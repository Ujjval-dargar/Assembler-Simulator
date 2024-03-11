The line number reported in the error takes into account blank lines in the input file.

Types of Errors:
- Label has space in between

>sta   rt: add s1, s2, s3

>start   : add s1, s2, s3

- Multiple labels defined
  
>start: add s1, s2, s3

>start: sub s1, s2, s3

- Label cannot be numeric
  
>1: add s1, s2, s3

- Label cannot be register ABI or Mnemonic
  
>add: sub s1, s2, s3

>s1: add s1, s2, s3

- Virtual Halt missing

- Missing opcode or no space between opcode and operands
  
>adds1s2s3

- Unknown mnemonic
  
>subsowkodw s1, s2, s3

- Immediate out of range

- Instruction has invalid number of operands
  
>add s1, s2

- Invalid syntax for instruction
>add 0, s1, s2
>lw s1, -100(s2

