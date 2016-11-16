### Hurricane Data Parsing

The NOAA currently has data on hurricanes and their various properties, dating back to 1851. The python program imports wind speeds, and uses those wind speeds along with the known intervals between observations to calculate Saffir-Simpson days per hurricane.

Hurricane data originally from hurdata.txt

consoleinput.txt has the commands necessary to generate plots graph/graph2.png based on the results of hurricanes.py

Usage:
```python3 hurdata.py hurdata.txt```

You can view an appropriately scaled gnuplot of output.txt by running:

```gnuplot gnuplot.txt```
