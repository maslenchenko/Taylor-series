Using Taylor series to calculate 1 (1 +sinx)  function


To calculate the value of 1 (1 +sinx)  function this formula was used:

![formula](https://user-images.githubusercontent.com/91615687/155279960-b0f9c7f2-0ac2-41e7-bd47-10a3ec460f0e.png)

Coding part:

To complete the task, three modules were written in Python3: user_sinx.py, taylor_sinx.py and test.py.
The first one simply calculates the value of certain x using the formula above. The function also accepts a number of terms. 
Here is the main code of the three modules. To improve the accuracy of calculations, 2 period is discarded. Then calculations repeat num times, for n == 1 to n == num. At first, the factorial of (2n-1) is calculated, and then the formula whose value is assigned to the variable sinx.

x_value = x_value%(2*pi) 
   sinx = 0
   for n in range(num):
       n += 1
       factorial = 1
       range1 = 2*n - 1
       for i in range(1,range1+1):
           factorial *= i
       sinx += (((-1)**(n-1))*x_value**(2*n-1))/factorial
   return 1/(1+sinx)

The module is designed to make it convenient for users to work with it.

The second module taylor_sinx.py uses the same code, but this time returns the result of using the series and a value of the function calculated using built-in function math.sin(). The function returns a tuple so that we can compare two values.
Arguments are the same: number of terms and x value.

The third module is created to compare accuracy using matplotlib.pyplot library and graphs. The first function is designed for small x intervals (create_plot_1()) and generates graphs both for Taylor series formula and built-in sin(). It accepts three arguments: seq_mem stands for the number of terms, and num - for how many x values (with the step of 0.1) the function will calculate. The same goes for the second function: it builds two graphs on bigger intervals. It accepts only one argument - the number of terms.

Accuracy of the calculations:

The following three graphs illustrate how the accuracy increases with the increase of the number of terms. In the majority of cases, ten terms are enough to achieve the accuracy of more than four decimal points. In general, sometimes it is enough five or even four terms (second graph), but there are some x values that deviate significantly from the correct values (picture 4, number of terms: 8). For graphs 5 and 6, the number of terms is 12, and here it is visible that schedules overlap.

![small_3](https://user-images.githubusercontent.com/91615687/155280014-a186ed2c-3b0b-4e72-8c22-6985e9051cb1.png)
![small_4](https://user-images.githubusercontent.com/91615687/155280031-772e4dbb-1fbc-4043-bcea-0be8a305fb99.png)
![small_10](https://user-images.githubusercontent.com/91615687/155280049-d0538c8d-6887-4dab-be38-b439fed8d3ae.png)
![big_8](https://user-images.githubusercontent.com/91615687/155280073-e7b199e5-2dda-4058-ad85-92e82a54a4d7.png)
![taylor_big_12](https://user-images.githubusercontent.com/91615687/155280095-d754790e-8230-4cd7-8cec-e382aab90bf0.png)
![both](https://user-images.githubusercontent.com/91615687/155280115-219030ef-f932-4c5a-b386-f336ceeb811c.png)

Short conclusion:

Taylor series for sinx give fairly accurate results. In general, ten terms are enough to achieve the accuracy of more than four decimal places. To improve the accuracy of calculations, 2 period is discarded. Up to ten terms, there are x values for which function values significantly differ from the normal ones, but, as mentioned before, this problem disappears after ten sequence members.




