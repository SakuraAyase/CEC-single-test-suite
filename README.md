# CEC-benchmarks
test suites of CECXXXX benchmarks


install steps:
1: decompose the file (解压缩)   
  
2: ipen the setup.py in txt mode and delete the code "libraries=["m"]" in setup.py (用txt格式打开setup.py，并且删掉其中的libraries=["m"]语句)   
3: install the setup.py via anaconda prompt, i.e. python setup.py install    
   (通过anaconda prompt，在文件根目录下运行setup.py文件，输入python setup.py install)     
   
   However the cec2005 test suite is not able to executed in python 3.6 or later version, with unknowledged reason.      
   
    reference: https://github.com/dmolina/cec2019comp100digit     
               https://github.com/Naeemeh146/CEC2013python   
