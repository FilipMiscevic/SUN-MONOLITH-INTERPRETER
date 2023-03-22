'''
    SUN MONOLITH EMERGENCY RESPONSE CODE COMMAND LINE INTERPRETER v1.0.0 (PYTHON-PROTOTYPE)
    ALSO AVAILABLE IN C AND FORTRAN-SF/k USING THE POLYWAT INTERPRETER (FORTHCOMING)
    DISTRIBUTED UNDER CC-BY 3.0 ATTRIBUTION NON-COMMERCIAL SHARE-ALIKE
    DISTRIBUTED BY EX LIBRIS PUBLISHING through GITHUB.COM/FilipMiscevic

    CONFIGURED FOR PLAINTEXT AND MYSQL OUTPUT

    AUTHOR: FILIP (ZORAN NIKOLA) MISCEVIC (FOUNTAINHEAD CONSULTING INC., TORONTO, ON, CANADA)
    CORRESPONDANCE AND LICENSING: MISCEVIC@CS.TORONTO.EDU

    DOCSTRING VERSION: 3-21-23
'''


import os, sys, datetime
import hashlib, binascii
from packaging.version import Version, parse


# hard-coded version control

ARG_VER = parse('1.0.0')
SM_VER  = parse('1.0.0')

### standard function library (standardized function definitions) ###

# ARCH
def archive(args, hash=None):
    if 'EOF' in args:
        args = args[args.index('EOF'):]
    return 'ARCH' # TODO: finish

# ARCHPDP
def arch_pdp(args, hash=None, **kwargs):
    return archive(args, hash) # TODO: implement tape backup, move to special args

# BCD
def ascii_to_bcd(args, hash=None):
    bcd = []
    for char in ' '.join(args):
        byte_string = bin(ord(char)).split('b')[1]
        if len(byte_string) < 8:
            byte_string = '0' * (8-len(byte_string)) + byte_string
        print(byte_string)
        first  = str(bin_to_decimal(byte_string[:4]))
        second = str(bin_to_decimal(byte_string[5:]))
        bcd.append(first+second)
    return ''.join(bcd)

def bcd_to_ascii(data):
    ascii = ''
    data = str(data)#.split(' ')
    for i in range(0,len(data)-1,2):
        first  = str(bin(int(data[i])).split('b')[1])
        second = str(bin(int(data[i+1])).split('b')[1])

        full = int(first + second, 2)

        print(full)

        ascii += chr( full + 48)
    return ascii

def bin_to_decimal(binary_num):
    decimal_num = 0
    for i in range(len(binary_num)):
        digit = binary_num[len(binary_num) - 1 - i]
        decimal_num += int(digit) * 2 ** i
    return decimal_num

def generate_bcd(data, hash = '', decimals = 0):
    '''
    Encode data into binary-coded decimal (BCD)
    '''
    res = 0
    for n, b in enumerate(reversed(bytes(hash + ' '.join(data), 'utf-8'))):
        res += (b & 0x0F) * 10 ** (n * 2 - decimals)
        res += (b >> 4) * 10 ** (n * 2 + 1 - decimals)
    return str(res)

# TODO: fix
def decode_bcd(message):
    message = str(message)
    decoded = ''
    for i in range(0,len(message)-1,2):
        char = int(message[i:i+2])
        decoded += chr(char + 48)
    return decoded

# BLOCK
def publish(args, hash=None):
    # publish the instruction set to apiXoracle under the unique message ID hash
    return 'PUBLISH'

# CODE
HOSPITAL_CODES = {
    'WHITE':'ViolentPatientOrHostage',
    'RED':'DispatchFire',
    'GREEN':'Evac',
    'BLUE':'CardiacArrest',
    'PINK':'NeonatalCardiacArrest',
    'BLACK':'BombThreat',
    'YELLOW':'MissingAdult',
    'AMBER':'MissingChild',
    'BROWN':'HAZMAT',
    'GREY':'UtilitiesLoss',
    'ORANGE':'ExternalMassCasualty'
}
def hospital_codes(args, hash=None):
    indices = [i for i,x in enumerate(args) if x.upper() == 'CODE']
    friendly_args = []
    for i in indices:
        arg = HOSPITAL_CODES[args[i+1].upper()]
        if i+2 < len(args)-1:
            second_arg = args[i+2].upper()
            if second_arg == 'TOTAL':
                arg = 'Total' + arg if arg in ['GREEN','RED'] else arg
                if i+3 < len(args)-1 and args[i+3].upper() == 'CANCEL':
                    arg += 'Cancel'
            elif second_arg == 'CANCEL':
                arg += 'Cancel'
        friendly_args.append(arg)
    return ' '.join(friendly_args)

# EXANDER
def killswitch(args, hash=None):
    return

def future(args):
    raise FutureWarning('WARNING: FUNCTION DEFINITION NOT IMPLEMENTED, STATUS: HALT')

### special function library (non-standard function definitions) ###

# PENDRESP
def publish_hold(args, hash=None, offset=0):
    return f'PENDRESP-{offset}'

# CHECKALLOC
def check_alloc(country_code, mode='USB', freq=88.3):
    return f'CHECKALLOC-{country_code}-{mode}-{freq}'

def format_version(ver):
    if ':::' in ver:
        return ver.split(':::')[1]
    else:
        return ver.upper().split('V')[1]

# V
def ensure_monolith_compat(ver):
    ver = format_version(ver)
    return ARG_VER >= parse(ver)

# v
def ensure_interpreter_compat(ver):
    ver = format_version(ver)
    return SM_VER >= parse(ver)

# OTP
def generate_otp(args, hash=None):
    return f'OTP-{hash}'

# SS4
def generate_rll_ss4(args, hash=None):
    # translate the message into the RLL-SS4 variant, with optional SOL and EOL transmission codes
    return 'SS4'

# SS5
def generate_rll_ss5(args, hash=None):
    # translate the message into the RLL-SS5 variant, with optional SOL and EOL transmission codes
    return 'SS5'

# MAYDAY
def mayday(args, hash=None):
    publish(args, hash)
    return check_alloc()

### apiXoracle ARG LIBRARY V1.0.0 ###

STANDARD_ARGS = {
    'ARCH':archive,
    'ARCHPDP':arch_pdp,
    'BCD':ascii_to_bcd,
    'CODE':hospital_codes,
    'OTP': generate_otp,
    'SS4': generate_rll_ss4,
    'SS5': generate_rll_ss5,
    'BLOCK':publish,
    'MAYDAY':mayday,
    'EXANDER':killswitch
}

SPECIAL_ARGS = {
    'PENDRESP': publish_hold,
    'CHECKALLOC': check_alloc,
    'V': ensure_monolith_compat,
    'v': ensure_interpreter_compat,

    #'HAM':future
}

SUPPORTED_ARGS = list(STANDARD_ARGS.keys()) + list(SPECIAL_ARGS.keys())

### executive functions ###

# hash functions
def sha256_digest(message):
    message = bytes(message, 'utf-8')
    return hashlib.sha256(message).hexdigest()

# interpreter functions
def to_unix(date):
    """
	Convert date to UNIX time since epoch in milliseconds.
	#param datetime.datetime date: datetime object
	#return: int corresponding to UNIX time
	"""
    return date if type(date) is not datetime.datetime else round(date.timestamp() * 1000)

def from_unix(timestamp):
    """
    Convert date to UNIX time since epoch in milliseconds.
    #param timestamp: time since epoch in milliseconds
    #return: datetime object corresponding to UNIX time
    """
    return datetime.datetime.fromtimestamp(timestamp / 1000)

def execute(func, args, kwargs):
    return func(*args,**kwargs)

def interpret(args):
    orig = args.strip().split()

    priority1 = []
    priority2 = []
    priority3 = []
    priority4 = []

    unsupported = []

    #hash variables
    filed  = None
    cchash = None

    offset = 0

    for arg in orig:
        argu = arg.upper()
        # halt on version incompatibility
        if 'V' in arg:
            if not ensure_monolith_compat(arg):
                raise InterruptedError("INCOMPATIBLE MONOLITH INSTRUCTION SET VERSION, STATUS: HALTED")
        elif 'v' in arg:
            if not ensure_interpreter_compat(arg):
                raise InterruptedError("INCOMPATIBLE INTERPRETER VERSION, STATUS: HALTED")
        # get the CC-HASH prime factorization, usually the first argument, to compute the message hash
        elif 'CC-HASH' in argu:
            if not cchash:
                cchash = arg.split(':::')[1]
        # then, sort args by hardware interrupt priority
        elif ':::' in arg and argu.split(':::')[0] in SUPPORTED_ARGS:
            priority1.append(argu)
        # get the env setup commands, if any
        elif '::' in arg and argu.split('::')[0] in SUPPORTED_ARGS:
            priority2.append(argu)
        # get time filed, also used for the hash
        elif 'FILED' in argu:
            if not filed:
                filed = arg.split(':')[1]
        elif ':' in arg and argu.split(':')[0] in SUPPORTED_ARGS:
            priority3.append(argu)
        elif 'PENDRESP' in argu:
            offset = argu.split('P')[2] #- to_unix(datetime.datetime.now())
        elif argu in SUPPORTED_ARGS:
            priority4.append(argu)
        #else:
        #    unsupported.append(arg)
        # finally, remove the arg
        #orig.remove(arg)

    # get database hash based on CC-HASH prime factorization and time filed
    if filed:
        #convert to UNIX timestamp
        try:
            filed = to_unix(filed)
        except:
            filed = to_unix(datetime.datetime.now())
    else:
        filed = to_unix(datetime.datetime.now())


    hash_string = '-'.join([cchash,str(filed),str(offset)])

    hash = sha256_digest(hash_string)
    vals = []
    val = None

    sorted_args = priority1 + priority2 + priority3 + priority4
    print(sorted_args)
    #print(unsupported)

    for exec_arg in sorted_args:
        if exec_arg in STANDARD_ARGS:
            func = STANDARD_ARGS[exec_arg]
            val = func(orig, hash)

            if val is None:
                raise InterruptedError(f"INVALID ARGS ({exec_arg}) OR KILLSWITCH ACTIVATED," +\
                                       f" STATUS: HALT \r\n\r\n{hash_string}\r\n{' '.join(vals)}")
            elif val not in vals:
                vals.append(val)
        else:
            parts = [s for s in exec_arg.split(':') if s]
            if parts[0] in SPECIAL_ARGS:
                func = SPECIAL_ARGS[parts[0]]
                arg  = []

                if len(parts) > 1:
                    arg += parts[1].split('-')

                kwargs = {} # TODO: add keyword support

                val = execute(func,arg,kwargs)

                if val is None:
                    raise InterruptedError(f"INVALID ARGS OR KILLSWITCH ACTIVATED," +\
                                           f" STATUS: HALT \r\n\r\n{hash_string}\r\n{' '.join(vals)}")
                elif val not in vals:
                    vals.append(val)

    return(' '.join([hash_string] + vals))

if __name__ == '__main__':
    message = sys.argv

    if len(message) <= 1:
        message = ' '.join(["CC-HASH:::-2^#x3x5^6",
                        "EOF",
                        "EOL",
                        "QED",
                        "ARCH",
                        "SH10151 PROPHET60091",
                        "APERATURE PSYCHOACOUSTIC LABORATORIES DBA SETI-GLaDOS@HOME",
                        "OTP",
                        "SS4",
                        "SS5",
                        "aapaed",
                        "FILED:feb242023-HAL-OXXIMAICCIKC",
                        "MONOLITH INSTRUCTION SET V1.0.0",
                        "(CC-BY)",
                        "pip::install-patentport",
                        "ARCHPDP",
                        "UNIXPROLOG",
                        "AT&T_NYC-0",
                        "### apiXoracle BLOCK PENDRESP1679647748 ###",
                        "POLYWATT INTERPRETER v0.9 ORIGinal",
                        "---...---...---...---___",
                        "### Sentinel global emergency response codes (cc-by-2025),",
                        "BCD backdoor",
                        "HAM:::USB89.3003 webSDR:::FI w:::1.5k30m CHECKALLOC:CA ###",
                        "CODE WHITE",
                        "CODE GREEN TOTAL CANCEL",
                        "EXANDER",
                        ])

    #bcd = generate_bcd(message) #,hash='-2^#x3x5^6-feb242023-HAL-OXXIMAICCIKC')
    #bcd2 = decode_bcd(bcd)
    #print(bcd,len(str(bcd)),len(message))
    #print(message+'\n',bcd2,len(str(bcd2)),len(message))

    digest = interpret(message)
    print(digest)
