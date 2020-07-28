# CEC-benchmarks
test suites of CECXXXX benchmarks
including cec2013single, cec2005single(void),cec2019 100 digit competition

install steps:      
      
1: decompose the file 
2: open the setup.py in txt mode and delete the code "libraries=["m"]" in setup.py
3: install the setup.py via anaconda prompt, i.e. python setup.py install    

   
安装步骤：
1：解压缩     
2：用txt格式打开setup.py，并且删掉其中的libraries=["m"]语句     
3：通过anaconda prompt，转到文件根目录下并输入python setup.py install以运行setup.py文件       
 
   However the cec2005 test suite is not able to executed in python 3.6 or later version, with unknowledged reason.         
   cec2005无法使用，原因不明emmmm       
   
    reference: https://github.com/dmolina/cec2019comp100digit     
               https://github.com/Naeemeh146/CEC2013python   
