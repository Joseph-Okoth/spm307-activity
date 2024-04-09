# Linear and Non-linear Equations

## 1. Create a Python program for solving the simultaneous equations below using Gaussian elimination and back-substitution: $${2w+x+4y+z=-4,}$$ $${3w+4x-y-z=3,}$$ $${w-4x+y+5z=9,}$$ $${2w-2x+y+3z=7.}$$

## 2. Modify the program you created above to incorporate pivoting (or you can write your own program from scratch if you prefer) and use it to solve the simultaneous equations below. $${x+4y+z=-4,}$$ $${3w+4x-y-z=3,}$$ $${w-4x+y+5z=9,}$$ $${2w-2x+y+3z=7.}$$

## 3. Modify the program you created above to calculate the LU decomposition (or you can write your own program fromscratch if you prefer) for equation 1.

## 4. Write a program to solve the equation $$x = 1-e^{−cx}$$ using the relaxation method for c = 2. Ensure the solution accuracy is at least $$10^{−6}$$ . Modify the program to calculate solutions for c ranging from 0 to 3 in steps of 0.01. Plot x against c and comment on the graph.

## 5. Write a program to solve $$5e^{−x} + x − 5 = 0$$ to an accuracy of $$10^{−6}$$ using the binary search method.

## 6. Consider the degree-six polynomial: $$P(x)=924x^{6}-2772x^{5}+3150x^{4}-1680x^{3}+420x^{2}-42x+1$$ 
## a) Plot $$P(x)$$ from $$x=0$$ to $$x=1$$ and then write a program using Newton's method to find the positions of all six roots with at least ten decimal places of accuracy.
## b) Modify the program to use the secant method to solve equation (3).

# Testing & Requirements

## Test Online:
Click the following link to test the solution 
https://colab.research.google.com/drive/1Aw_PVxv1igP3YG35AQOMuCRQ_5x5r9-p?usp=sharing


## Local Functionality

1. Install Python in your local environment

2. Clone the repository
    ```bash 
    git clone https://github.com/jonyach/spm307-activity/activity3

3. Running the codes
    ```bash
    python3 path/to/the/python/file

Example

    ```bash
    python3 ./spm307-activity/activity3/binarysearch.py