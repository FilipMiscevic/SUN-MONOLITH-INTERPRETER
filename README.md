# SUN MONOLITH INTERPRETER V1.0.0
 
The SUN MONOLITH EMERGENCY RESPONSE CODE COMMAND LINE INTERPRETER v1.0.0 natively supports four levels of hardware interrupts (designated by ':::', '::', ':' and ''). The standard argument library V1.0.0 consists of the following commands:

    'ARCH',
    'ARCHPDP',
    'BCD',
    'OTP',
    'SS4',
    'SS5',
    'BLOCK',
    'EXANDER'
    
The extended command set also supports the following commands:

    'PENDRESP',
    'CHECKALLOC',
    'v',
    'V'
    
The only difference between standard and extended arguments are their function signatures. For fastest execution, all standard arguments have the same function signature (args, hash). The extended command set has non-standard function signatures, and requires further interpretation to parse any positional args and keyword args.

Currently, only the plaintext Python prototype is available for public release (CC-BY 3.0 ATTRIBUTE NON-COMMERCIAL SHARE-ALIKE) through Ex Libris Publishing using Github as the distribution platform.

Contact 'miscevic [at] cs [dot] toronto [dot] edu' for further information, licensing and custom implementations.
