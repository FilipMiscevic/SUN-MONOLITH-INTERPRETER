# SUN MONOLITH INTERPRETER v1.0.0
 
Inspired by military monolith messaging architectures, the SUN MONOLITH EMERGENCY RESPONSE CODE COMMAND LINE INTERPRETER v1.0.0 is a custom NoSQL variant designed for potential use in hospitals, avionics, and other applications requiring mission-critical, near real-time execution. It is optimized for deployment on the blockchain and other API3-compliant applications, along with support for command line, MySQL, and plaintext piping.

It natively supports four levels of hardware interrupts (designated within a command by ':::', '::', ':' and ''). The standard apiXoracle argument library V1.0.0 consists of the following commands:

    'ARCH',
    'ARCHPDP',
    'BCD',
    'CODE', #  support for hospital-specific codes
    'OTP',
    'SS4',
    'SS5',
    'BLOCK',
    'MAYDAY',
    'EXANDER'
    
The extended command set also supports the following commands:

    'PENDRESP',
    'CHECKALLOC',
    'v', # ensure interpreter compatibility (version control)
    'V'  # ensure apiXoracle instruction set compatibility
    
The only difference between standard and extended arguments are their function signatures. For fastest execution, all standard arguments have the same function signature ```func(args, hash)```. The extended command set has non-standard function signatures, and requires further interpretation to parse any positional and keyword args. Note that by design, even standard args have access to the entire message and can therefore further interpret it if necessary, as in the case of hospital codes, which consist of a two- or three-word phrase to designate a specific response code (e.g., 'CODE RED', 'CODE GREEN TOTAL', or 'CODE WHITE CANCEL').

Currently, only the plaintext Python prototype is available for public release (CC-BY 3.0 ATTRIBUTE NON-COMMERCIAL SHARE-ALIKE, overriding the standard GNU-GPL 3.0 license) through Ex Libris Publishing using Github as the distribution platform.

Contact ```miscevic [at] cs [dot] toronto [dot] edu``` for further information, licensing and custom implementations.
