# SA-Project
Example of using salib for sensitivity analysis.
## Example :
In this example, we will perform a Sobol’ sensitivity analysis of a polynomial function, shown below.

<img
  src="https://latex.codecogs.com/svg.image?f(x)&space;=&space;ax^{2}&space;&plus;&space;bx&space;&plus;&space;c" title=""
/>

with :

<img
  src="https://latex.codecogs.com/svg.image?a&space;\in&space;\left&space;[&space;0,1&space;\right&space;]&space;,&space;b&space;\in&space;\left&space;[&space;-1,0&space;\right&space;]&space;,&space;c&space;\in&space;\left&space;[&space;1,2&space;\right&space;]" title=""
/>
### Basic Plotting :
Basic plotting facilities are provided for convenience.

![index](https://user-images.githubusercontent.com/74584503/203494824-eb60429e-0ba4-46b3-bf57-15b2548d4803.png)

## SALib Paper

```text
Herman, J. and Usher, W. (2017) SALib: An open-source Python library for sensitivity analysis. 
Journal of Open Source Software, 2(9).
```
The library includes multiple methods. For a good review of sensitivity analysis methods, I suggest this paper:
```text
Pianosi, Francesca, et al. "Sensitivity analysis of environmental models: A systematic review with 
practical workflow." Environmental Modelling & Software 79 (2016): 214-232.
```
