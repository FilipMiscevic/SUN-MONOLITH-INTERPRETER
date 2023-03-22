# SUN MONOLITH INTERPRETER v1.0.0
 
Inspired by robust monolith messaging architectures developed for defense purposes, the SUN MONOLITH EMERGENCY RESPONSE CODE COMMAND LINE INTERPRETER v1.0.0 employs a custom NoSQL variant designed for potential use in hospitals, avionics, and other applications requiring mission-critical, near real-time execution and subsequent indelible archiving. It is therefore optimized for deployment on the blockchain and other API3-compliant applications, along with support for command line, database (e.g., SQL-based), and plaintext piping.

It natively supports four levels of hardware interrupts (designated within a command by ':::', '::', ':' and ''). The standard apiXoracle(C) argument library V1.0.0 consists of the following commands:

    'ARCH',   # archive message to a specified server
    'ARCHPDP',# archive using legacy equipment (e.g., PDP tape backups)
    'BCD',    # encode plaintext messages using the digits 0-9, inclusive
    'CODE',   # support for hospital-specific code parsing
    'OTP',    # generate a one-time pad for secure message encryption
    'SS4',    # telephony signalling system 4 (Bell Telephone Labs, Inc.)
    'SS5',    # telephony signalling system 5 (Bell Telephone Labs, Inc.)
    'BLOCK',  # publish message to the blockchain
    'WATALL', # real-time FORTRAN and C interpretation (IPR)
    'WATCOM', # C interpreter
    'WATFIV', # FORTRAN interpreter
    'POLYWAT',# alias for 'WATALL' command
    'MAYDAY', # standard avionics distress signal
    'EXANDER' # killswitch: parse up to argument position but do not 'PUBLISH'
    
The extended command set also supports the following commands:

    'PENDRESP',  # archive but do not publish message until UNIX time reached
    'CHECKALLOC',# find an appropriate messaging band for radio communications based on country code, transmission mode and desired destination
    'v',         # ensure interpreter compatibility (hard-coded version control)
    'V'          # ensure apiXoracle(C) instruction set compatibility
    
The only difference between standard and extended arguments are their function signatures. For fastest execution, all standard arguments have the same function signature ```func(args, hash=None)```. The extended command set has non-standard function signatures, and requires further direct interpretation to parse any positional and keyword args. 

Note that by design, standard args have access to the entire message and can therefore provide further interpretation if necessary, as in the case of hospital codes, which consist of a two- or three-word phrase to designate a specific response code (e.g., 'CODE RED', 'CODE GREEN TOTAL', or 'CODE WHITE CANCEL'). These additional argument flags or codewords can be processed by designated functions called by the SUN MONOLITH interpreter, but the SUN MONOLITH interpreter itself will ignore these argument flags, as they are not directly supported (by default) in the standard or extended command set. In other words, in the case of hospital code parsing, 'CODE' will trigger the function call that will then recognize additional positional arguments as standard hospital codes (such as 'WHITE', 'BLACK', 'PINK')--however, the specific codes themselves are not part of the standard or extended command set because they do not themselves require additional function calls outside of the original 'CODE' call. This improves overall interpreter performance, and partial or malformed codes (such as the presence of the keyphrase 'WHITE' without being preceeded by 'CODE') will simply be removed from the call stack.

Currently, only the plaintext Python prototype is available for open-source public release (CC-BY 3.0 ATTRIBUTE NON-COMMERCIAL SHARE-ALIKE, overriding the standard GNU-GPL 3.0 license) through Ex Libris Publishing using Github as the preferred distribution platform.

Contact ```miscevic [at] cs [dot] toronto [dot] edu``` for further information, licensing and custom implementations. apiXoracle(C) is pending copyright.
