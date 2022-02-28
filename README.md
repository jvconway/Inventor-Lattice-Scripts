# Inventor Lattice Scripts
 Scripts to create Inventor assembly based on Bmad Lattice Layout 

# v1 - Dave Burke - UCS's
 This method was developed and used by Dave Burke in the design of the CBETA ERL at Cornell. His documentation and relevant files are included. I believe this is a good method for mature accelerator designs and detailed engineering.

# v2 - Joe Conway - UCS's
 This was my first working version of the project. It requires conversion of the *.layout_table file to *.xlsx. It also uses the UCS method. This method is only included for historical documentation. It is much slower than v3 (hours v minutes) so not good for preliminary studies and has none of the positive feature's of Dave's method which make it good for detailed engineering.


# v3 - Joe Conway - Direct to Asm from CSV
 I developed this method for use in preliminary lattice design studies for the Electron Ion Collider Strong Hadron Cooling ERL (EIC SHC ERL).  After initial set up, it creates an assembly of a lattice in under 10 minutes.  It can be used to do space studies and take measurements, but cannot be modified/adjusted like Dave's method. A new lattice *.layout_table file must be generated and this method run from scratch (again < 10 minutes) to generate a new assembly.

# Introduction
Importing a Bmad lattice into Autodesk Inventor is an important tool for physicists and engineers designing a new machine from preliminary design stages (making sure the machine will fit into the space available), to detailed engineering design (including vacuum chamber and magnet girder design), to machine survey during commissioning.

A *.layout\_table file generated by Bmad consists of a row for each element defined in the lattice defining the element name, type, position in space relative to an origin point, and any other information potentially important.

Through the use of iLogic scripts in Autodesk Inventor, a *.layout\_table can be used to generate 3D models of individual elements and then place those and other elements in an assembly. There are 2 procedures used by different projects to do this which will be described in this document.  One uses User Coordinate Systems (UCSs) and may be more appropriate for more mature designs, and the other places components directly in assemblies. This method is much faster and may be more appropriate for preliminary designs.

*.layout\_table files are also being used to generate 3D models of lattices in Blender and procedures to import Inventor models into Blender and Blender models into Inventor are being created for samity checks and to be able to take advantage of each program's unique strong points.

# Bmad Lattice
Bmad is one of many tools a physicist can use to design or analyze a particle accelerator. In relation to this document Bmad was used to design the lattice for the CBETA project at Cornell, a joint effort between CLASSE and BNL, and is being used by XELERA Research to help design the ERL to be used for Strong Hadron Cooling at the Electron Ion Cooler at BNL. A link for Bmad documentation can be found in the References Section.

For the purposes of this document, Bmad can output a *.layout\_table file that consists of data describing features of the elements of the lattice. We are most interested in the elements' name, type, XYZ position, theta, phi, psi, orientation, length, and bend angle (if appropriate).  Other properties may be described in the file that we do not need, or may be added to the file by request to the lattice designer.

The element locations in the *.layout\_table file define the center of the element along its length on the beam path.  Section 15.2 of the Bmad Documentation describes the coordinate system used by Bmad and in the *.layout\_table file.

# Inventor Coordinate Systems
Coordinate systems in a CAD program are convenient for quickly and accurately locating components. However, forethought and planning are important when setting up the CAD models. Part models must be created with the proper orientation to the global coordinate system in mind. 

User coordinate systems in Inventor can be a powerful tool in this process.  UCS's can be easily be placed by a script in an Inventor assembly (almost) directly using the same XYZ and theta, phi, psi parameters that are defined in the Bmad lattice. A UCS can be included in the part model, and when placing the part in the assembly, the part UCS can be very easily constrained to the UCS previously placed in the correct position and orientation.  Other elements such as pedestals, girders, or vacuum chambers may be constrained to the UCS's to define and preserve their position. Additionally, the parameters of UCS's are easily updated if changes to the lattice are made and if done carefully this method allows for small adjustments to be made and all relevant parts to be updated.  This method was used by Dave Burke in the design of CBETA at Cornell.

#References
1. Bmad Software Toolkit for Charged-Particle and X-Ray Simulations. http://www.lepp.cornell.edu/~dcs/bmad/overview.html
