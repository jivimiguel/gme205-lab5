# Polymorphism in Spatial Object Systems
## Overview
This laboratory applies the four pillars of Object-Oriented Programming (OOP) to a spatial system. The focus of this Lab is the polymorphism, where different spatial objects `Parcel`, `Building`, and `Road` share the same method name `effective_area()` but compute area differently.

This allows the program to avoid logic and remain scalable as new classes are added

## Environment Setup
- Python 3.14
- `shapely`

---

## How to Run
1. Activate the virtual environment
2. Run `run_lab5.py`
3. Run `demo.py` (Optional, this is just to show how polymorphism works)

---
## Reflection
Polymorphism appears in my system when different spatial objects, such as Parcel, Building, and Road use the same method name, `effective_area()`, but compute their areas in different ways. Even though these objects are not the same type, the program can loop through them and call the same method, and each object automatically performs the correct calculation. This shared method call is the main point where polymorphism is used in the program.

Polymorphism removes conditional logic from my analysis code because I no longer need to write long if or elif statements checking which type of object I am working with. Instead of deciding in the analysis code how each feature should compute its area, I just call f.`effective_area()` and the object handles the correct behavior on its own. This keeps the analysis simple and prevents the conditional explosion” mentioned in the lab instructions.

The OOP pillar that allows different spatial classes to share the same method name is `polymorphism`, supported by inheritance and abstraction. The base `class SpatialObject` defines the method that subclasses must implement, which allows them to share the same method name but behave differently when the method is called.

It is better for objects to compute their own area because each feature type has its own definition of area. For example, parcels use polygon area, buildings multiply footprint area by number of floors, and roads use buffered width. If I tried to compute all of these in one place, the code would become messy and full of conditions. Putting the behavior inside each object makes the program cleaner, easier to maintain, and easier to extend.

If I add a new class tomorrow such as `River` the only change needed is to create a new class in `spatial.py` that inherits from `SpatialObject` and implements its own `effective_area()` method. I do not need to change `run_lab5.py` because it already works with any object that has this method. This shows that the system is designed to be easy to extend with new spatial types.