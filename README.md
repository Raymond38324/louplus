把Conda环境导出
```
conda env export > environment.yaml 
```
把environment.yaml中的环境导入
```
conda env create -f environment.yaml
```
启动虚拟环境
```
source activate seiya
```
