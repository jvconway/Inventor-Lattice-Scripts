# v4 - Joe Conway - Direct to Asm from CSV
I developed this method for use in preliminary lattice design studies for the Electron Ion Collider Strong Hadron Cooling ERL (EIC SHC ERL).  After initial set up, it creates an assembly of a lattice in under 10 minutes.  It can be used to do space studies and take measurements, but cannot be modified/adjusted like Dave's method. A new lattice \*.layout_table file must be generated and this method run from scratch (again < 10 minutes) to generate a new assembly.

# Procedure
1. Acquire *.layout_table file from lattice designer
2. Create "template" part files for all elements.  For one-off elements or imaginary elements, create a part and save it with the proper name.  For common elements, like quads or bends, create a base model with, for example, the length parameterized. Create/Copy iLogic Rule 0 for these parts that parses \*.layout_table file and creates individual parts for each unique element.
3. Create assembly file, create/copy iLogic Rule 0 that opens element "template" files and runs their Rule 0's creating all of the necessary unique part files, parses \*.layout_table file, and places the correct element part file in the correct location.

# Pros
- After initial setup each iteration is fast (<10 minutes)

# Cons
- Cannot adjust location of elements in assembly, if any changes are needed, must re-do Step 3 with new \*.layout_table file 
