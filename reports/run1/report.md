# Run 1  
- loss = 'categorical\_crossentropy'  
- optimizer = 'adam'  
- batch\_size = 128  
- epochs = 1000  
- earlystop = EarlyStopping(monitor='val\_acc',min\_delta=.01, patience=20)  

#### Summary Results  
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>epochs</th>      <th>time</th>      <th>trainacc</th>      <th>valacc</th>    </tr>    <tr>      <th>model</th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>model1</th>      <td>44</td>      <td>0m:2s</td>      <td>0.269867</td>      <td>0.175121</td>    </tr>    <tr>      <th>model2</th>      <td>97</td>      <td>0m:5s</td>      <td>0.882211</td>      <td>0.688406</td>    </tr>    <tr>      <th>model3</th>      <td>94</td>      <td>0m:6s</td>      <td>0.929810</td>      <td>0.687198</td>    </tr>    <tr>      <th>model4</th>      <td>74</td>      <td>0m:6s</td>      <td>0.931827</td>      <td>0.693237</td>    </tr>  </tbody></table>  

## Model1  

#### Architecture  
- Flatten
- Dense 26 softmax  
 
#### Training Plot 
![](model1_training.png)  

#### Layer 2 Weights (Dense) - Sample Images 
![](model1_layer2_weights.png)  

#### Letter Accuracy 
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>TrainCount</th>      <th>TrainCorrect</th>      <th>Train%Correct</th>      <th>ValCount</th>      <th>ValCorrect</th>      <th>Val%Correct</th>    </tr>    <tr>      <th>0</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>A</th>      <td>275</td>      <td>189</td>      <td>0.69</td>      <td>92</td>      <td>45</td>      <td>0.49</td>    </tr>    <tr>      <th>B</th>      <td>54</td>      <td>1</td>      <td>0.02</td>      <td>18</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>C</th>      <td>102</td>      <td>32</td>      <td>0.31</td>      <td>34</td>      <td>4</td>      <td>0.12</td>    </tr>    <tr>      <th>D</th>      <td>99</td>      <td>0</td>      <td>0.00</td>      <td>33</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>E</th>      <td>214</td>      <td>32</td>      <td>0.15</td>      <td>71</td>      <td>7</td>      <td>0.10</td>    </tr>    <tr>      <th>F</th>      <td>41</td>      <td>0</td>      <td>0.00</td>      <td>14</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>G</th>      <td>66</td>      <td>5</td>      <td>0.08</td>      <td>22</td>      <td>1</td>      <td>0.05</td>    </tr>    <tr>      <th>H</th>      <td>91</td>      <td>13</td>      <td>0.14</td>      <td>30</td>      <td>2</td>      <td>0.07</td>    </tr>    <tr>      <th>I</th>      <td>162</td>      <td>47</td>      <td>0.29</td>      <td>54</td>      <td>13</td>      <td>0.24</td>    </tr>    <tr>      <th>J</th>      <td>31</td>      <td>0</td>      <td>0.00</td>      <td>10</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>K</th>      <td>40</td>      <td>5</td>      <td>0.12</td>      <td>13</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>L</th>      <td>100</td>      <td>3</td>      <td>0.03</td>      <td>34</td>      <td>2</td>      <td>0.06</td>    </tr>    <tr>      <th>M</th>      <td>76</td>      <td>17</td>      <td>0.22</td>      <td>25</td>      <td>3</td>      <td>0.12</td>    </tr>    <tr>      <th>N</th>      <td>167</td>      <td>82</td>      <td>0.49</td>      <td>56</td>      <td>21</td>      <td>0.38</td>    </tr>    <tr>      <th>O</th>      <td>174</td>      <td>32</td>      <td>0.18</td>      <td>58</td>      <td>7</td>      <td>0.12</td>    </tr>    <tr>      <th>P</th>      <td>78</td>      <td>12</td>      <td>0.15</td>      <td>26</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>Q</th>      <td>12</td>      <td>0</td>      <td>0.00</td>      <td>4</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>R</th>      <td>185</td>      <td>68</td>      <td>0.37</td>      <td>62</td>      <td>13</td>      <td>0.21</td>    </tr>    <tr>      <th>S</th>      <td>162</td>      <td>65</td>      <td>0.40</td>      <td>54</td>      <td>19</td>      <td>0.35</td>    </tr>    <tr>      <th>T</th>      <td>154</td>      <td>22</td>      <td>0.14</td>      <td>51</td>      <td>8</td>      <td>0.16</td>    </tr>    <tr>      <th>U</th>      <td>49</td>      <td>3</td>      <td>0.06</td>      <td>17</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>V</th>      <td>38</td>      <td>1</td>      <td>0.03</td>      <td>13</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>W</th>      <td>34</td>      <td>12</td>      <td>0.35</td>      <td>11</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>X</th>      <td>25</td>      <td>0</td>      <td>0.00</td>      <td>9</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>Y</th>      <td>32</td>      <td>1</td>      <td>0.03</td>      <td>11</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>Z</th>      <td>18</td>      <td>2</td>      <td>0.11</td>      <td>6</td>      <td>0</td>      <td>0.00</td>    </tr>  </tbody></table>  

#### Accurate Validation Prediction - Sample Images 
![](model1_correct.png)  

#### Inaccurate Validation Prediction - Sample Images 
![](model1_incorrect.png)  

## Model2  

#### Architecture 
- Flatten
- Dense 100 relu  
- Dense 26 softmax  
 
#### Training Plot 
![](model2_training.png)  

#### Layer 2 Weights (Dense) - Sample Images 
![](model2_layer2_weights.png)  

#### Layer 3 Weights (Dense) - Sample Images 
![](model2_layer3_weights.png)  

#### Letter Accuracy 
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>TrainCount</th>      <th>TrainCorrect</th>      <th>Train%Correct</th>      <th>ValCount</th>      <th>ValCorrect</th>      <th>Val%Correct</th>    </tr>    <tr>      <th>0</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>A</th>      <td>275</td>      <td>265</td>      <td>0.96</td>      <td>92</td>      <td>72</td>      <td>0.78</td>    </tr>    <tr>      <th>B</th>      <td>54</td>      <td>31</td>      <td>0.57</td>      <td>18</td>      <td>7</td>      <td>0.39</td>    </tr>    <tr>      <th>C</th>      <td>102</td>      <td>97</td>      <td>0.95</td>      <td>34</td>      <td>27</td>      <td>0.79</td>    </tr>    <tr>      <th>D</th>      <td>99</td>      <td>80</td>      <td>0.81</td>      <td>33</td>      <td>18</td>      <td>0.55</td>    </tr>    <tr>      <th>E</th>      <td>214</td>      <td>202</td>      <td>0.94</td>      <td>71</td>      <td>54</td>      <td>0.76</td>    </tr>    <tr>      <th>F</th>      <td>41</td>      <td>26</td>      <td>0.63</td>      <td>14</td>      <td>4</td>      <td>0.29</td>    </tr>    <tr>      <th>G</th>      <td>66</td>      <td>56</td>      <td>0.85</td>      <td>22</td>      <td>10</td>      <td>0.45</td>    </tr>    <tr>      <th>H</th>      <td>91</td>      <td>73</td>      <td>0.80</td>      <td>30</td>      <td>13</td>      <td>0.43</td>    </tr>    <tr>      <th>I</th>      <td>162</td>      <td>143</td>      <td>0.88</td>      <td>54</td>      <td>44</td>      <td>0.81</td>    </tr>    <tr>      <th>J</th>      <td>31</td>      <td>23</td>      <td>0.74</td>      <td>10</td>      <td>1</td>      <td>0.10</td>    </tr>    <tr>      <th>K</th>      <td>40</td>      <td>34</td>      <td>0.85</td>      <td>13</td>      <td>9</td>      <td>0.69</td>    </tr>    <tr>      <th>L</th>      <td>100</td>      <td>93</td>      <td>0.93</td>      <td>34</td>      <td>25</td>      <td>0.74</td>    </tr>    <tr>      <th>M</th>      <td>76</td>      <td>68</td>      <td>0.89</td>      <td>25</td>      <td>17</td>      <td>0.68</td>    </tr>    <tr>      <th>N</th>      <td>167</td>      <td>149</td>      <td>0.89</td>      <td>56</td>      <td>46</td>      <td>0.82</td>    </tr>    <tr>      <th>O</th>      <td>174</td>      <td>167</td>      <td>0.96</td>      <td>58</td>      <td>48</td>      <td>0.83</td>    </tr>    <tr>      <th>P</th>      <td>78</td>      <td>71</td>      <td>0.91</td>      <td>26</td>      <td>20</td>      <td>0.77</td>    </tr>    <tr>      <th>Q</th>      <td>12</td>      <td>6</td>      <td>0.50</td>      <td>4</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>R</th>      <td>185</td>      <td>167</td>      <td>0.90</td>      <td>62</td>      <td>37</td>      <td>0.60</td>    </tr>    <tr>      <th>S</th>      <td>162</td>      <td>159</td>      <td>0.98</td>      <td>54</td>      <td>44</td>      <td>0.81</td>    </tr>    <tr>      <th>T</th>      <td>154</td>      <td>135</td>      <td>0.88</td>      <td>51</td>      <td>41</td>      <td>0.80</td>    </tr>    <tr>      <th>U</th>      <td>49</td>      <td>43</td>      <td>0.88</td>      <td>17</td>      <td>13</td>      <td>0.76</td>    </tr>    <tr>      <th>V</th>      <td>38</td>      <td>33</td>      <td>0.87</td>      <td>13</td>      <td>6</td>      <td>0.46</td>    </tr>    <tr>      <th>W</th>      <td>34</td>      <td>31</td>      <td>0.91</td>      <td>11</td>      <td>5</td>      <td>0.45</td>    </tr>    <tr>      <th>X</th>      <td>25</td>      <td>16</td>      <td>0.64</td>      <td>9</td>      <td>4</td>      <td>0.44</td>    </tr>    <tr>      <th>Y</th>      <td>32</td>      <td>27</td>      <td>0.84</td>      <td>11</td>      <td>5</td>      <td>0.45</td>    </tr>    <tr>      <th>Z</th>      <td>18</td>      <td>11</td>      <td>0.61</td>      <td>6</td>      <td>0</td>      <td>0.00</td>    </tr>  </tbody></table>  

#### Accurate Validation Prediction - Sample Images 
![](model2_correct.png)  

#### Inaccurate Validation Prediction - Sample Images 
![](model2_incorrect.png)  

## Model3  

#### Architecture 
- Flatten
- Dense 100 relu  
- Dense 100 relu  
- Dense 26 softmax  

#### Training Plot 
![](model3_training.png)  

#### Layer 2 Weights (Dense) - Sample Images 
![](model3_layer2_weights.png)  

#### Layer 3 Weights (Dense) - Sample Images 
![](model3_layer3_weights.png)  

#### Layer 4 Weights (Dense) - Sample Images 
![](model3_layer4_weights.png)  

#### Letter Accuracy 
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>TrainCount</th>      <th>TrainCorrect</th>      <th>Train%Correct</th>      <th>ValCount</th>      <th>ValCorrect</th>      <th>Val%Correct</th>    </tr>    <tr>      <th>0</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>A</th>      <td>275</td>      <td>269</td>      <td>0.98</td>      <td>92</td>      <td>70</td>      <td>0.76</td>    </tr>    <tr>      <th>B</th>      <td>54</td>      <td>43</td>      <td>0.80</td>      <td>18</td>      <td>7</td>      <td>0.39</td>    </tr>    <tr>      <th>C</th>      <td>102</td>      <td>93</td>      <td>0.91</td>      <td>34</td>      <td>25</td>      <td>0.74</td>    </tr>    <tr>      <th>D</th>      <td>99</td>      <td>93</td>      <td>0.94</td>      <td>33</td>      <td>18</td>      <td>0.55</td>    </tr>    <tr>      <th>E</th>      <td>214</td>      <td>209</td>      <td>0.98</td>      <td>71</td>      <td>56</td>      <td>0.79</td>    </tr>    <tr>      <th>F</th>      <td>41</td>      <td>34</td>      <td>0.83</td>      <td>14</td>      <td>9</td>      <td>0.64</td>    </tr>    <tr>      <th>G</th>      <td>66</td>      <td>63</td>      <td>0.95</td>      <td>22</td>      <td>11</td>      <td>0.50</td>    </tr>    <tr>      <th>H</th>      <td>91</td>      <td>79</td>      <td>0.87</td>      <td>30</td>      <td>15</td>      <td>0.50</td>    </tr>    <tr>      <th>I</th>      <td>162</td>      <td>147</td>      <td>0.91</td>      <td>54</td>      <td>34</td>      <td>0.63</td>    </tr>    <tr>      <th>J</th>      <td>31</td>      <td>24</td>      <td>0.77</td>      <td>10</td>      <td>2</td>      <td>0.20</td>    </tr>    <tr>      <th>K</th>      <td>40</td>      <td>38</td>      <td>0.95</td>      <td>13</td>      <td>6</td>      <td>0.46</td>    </tr>    <tr>      <th>L</th>      <td>100</td>      <td>97</td>      <td>0.97</td>      <td>34</td>      <td>30</td>      <td>0.88</td>    </tr>    <tr>      <th>M</th>      <td>76</td>      <td>68</td>      <td>0.89</td>      <td>25</td>      <td>14</td>      <td>0.56</td>    </tr>    <tr>      <th>N</th>      <td>167</td>      <td>158</td>      <td>0.95</td>      <td>56</td>      <td>47</td>      <td>0.84</td>    </tr>    <tr>      <th>O</th>      <td>174</td>      <td>164</td>      <td>0.94</td>      <td>58</td>      <td>45</td>      <td>0.78</td>    </tr>    <tr>      <th>P</th>      <td>78</td>      <td>72</td>      <td>0.92</td>      <td>26</td>      <td>18</td>      <td>0.69</td>    </tr>    <tr>      <th>Q</th>      <td>12</td>      <td>10</td>      <td>0.83</td>      <td>4</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>R</th>      <td>185</td>      <td>169</td>      <td>0.91</td>      <td>62</td>      <td>35</td>      <td>0.56</td>    </tr>    <tr>      <th>S</th>      <td>162</td>      <td>160</td>      <td>0.99</td>      <td>54</td>      <td>45</td>      <td>0.83</td>    </tr>    <tr>      <th>T</th>      <td>154</td>      <td>149</td>      <td>0.97</td>      <td>51</td>      <td>44</td>      <td>0.86</td>    </tr>    <tr>      <th>U</th>      <td>49</td>      <td>44</td>      <td>0.90</td>      <td>17</td>      <td>13</td>      <td>0.76</td>    </tr>    <tr>      <th>V</th>      <td>38</td>      <td>36</td>      <td>0.95</td>      <td>13</td>      <td>9</td>      <td>0.69</td>    </tr>    <tr>      <th>W</th>      <td>34</td>      <td>31</td>      <td>0.91</td>      <td>11</td>      <td>3</td>      <td>0.27</td>    </tr>    <tr>      <th>X</th>      <td>25</td>      <td>19</td>      <td>0.76</td>      <td>9</td>      <td>5</td>      <td>0.56</td>    </tr>    <tr>      <th>Y</th>      <td>32</td>      <td>27</td>      <td>0.84</td>      <td>11</td>      <td>6</td>      <td>0.55</td>    </tr>    <tr>      <th>Z</th>      <td>18</td>      <td>15</td>      <td>0.83</td>      <td>6</td>      <td>2</td>      <td>0.33</td>    </tr>  </tbody></table>  

#### Accurate Validation Prediction - Sample Images 
![](model3_correct.png)  

#### Inaccurate Validation Prediction - Sample Images 
![](model3_incorrect.png)  

## Model4  

#### Architecture 
- Flatten
- Dense 100 relu  
- Dense 100 relu  
- Dense 100 relu  
- Dense 26 softmax  

#### Training Plot 
![](model4_training.png)  

#### Layer 2 Weights (Dense) - Sample Images 
![](model4_layer2_weights.png)  

#### Layer 3 Weights (Dense) - Sample Images 
![](model4_layer3_weights.png)  

#### Layer 4 Weights (Dense) - Sample Images 
![](model4_layer4_weights.png)  

#### Layer 5 Weights (Dense) - Sample Images 
![](model4_layer5_weights.png)  

#### Letter Accuracy 
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>TrainCount</th>      <th>TrainCorrect</th>      <th>Train%Correct</th>      <th>ValCount</th>      <th>ValCorrect</th>      <th>Val%Correct</th>    </tr>    <tr>      <th>0</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>A</th>      <td>275</td>      <td>264</td>      <td>0.96</td>      <td>92</td>      <td>65</td>      <td>0.71</td>    </tr>    <tr>      <th>B</th>      <td>54</td>      <td>46</td>      <td>0.85</td>      <td>18</td>      <td>10</td>      <td>0.56</td>    </tr>    <tr>      <th>C</th>      <td>102</td>      <td>99</td>      <td>0.97</td>      <td>34</td>      <td>25</td>      <td>0.74</td>    </tr>    <tr>      <th>D</th>      <td>99</td>      <td>94</td>      <td>0.95</td>      <td>33</td>      <td>24</td>      <td>0.73</td>    </tr>    <tr>      <th>E</th>      <td>214</td>      <td>205</td>      <td>0.96</td>      <td>71</td>      <td>52</td>      <td>0.73</td>    </tr>    <tr>      <th>F</th>      <td>41</td>      <td>34</td>      <td>0.83</td>      <td>14</td>      <td>9</td>      <td>0.64</td>    </tr>    <tr>      <th>G</th>      <td>66</td>      <td>58</td>      <td>0.88</td>      <td>22</td>      <td>13</td>      <td>0.59</td>    </tr>    <tr>      <th>H</th>      <td>91</td>      <td>83</td>      <td>0.91</td>      <td>30</td>      <td>20</td>      <td>0.67</td>    </tr>    <tr>      <th>I</th>      <td>162</td>      <td>157</td>      <td>0.97</td>      <td>54</td>      <td>42</td>      <td>0.78</td>    </tr>    <tr>      <th>J</th>      <td>31</td>      <td>28</td>      <td>0.90</td>      <td>10</td>      <td>2</td>      <td>0.20</td>    </tr>    <tr>      <th>K</th>      <td>40</td>      <td>37</td>      <td>0.92</td>      <td>13</td>      <td>8</td>      <td>0.62</td>    </tr>    <tr>      <th>L</th>      <td>100</td>      <td>95</td>      <td>0.95</td>      <td>34</td>      <td>25</td>      <td>0.74</td>    </tr>    <tr>      <th>M</th>      <td>76</td>      <td>72</td>      <td>0.95</td>      <td>25</td>      <td>16</td>      <td>0.64</td>    </tr>    <tr>      <th>N</th>      <td>167</td>      <td>160</td>      <td>0.96</td>      <td>56</td>      <td>44</td>      <td>0.79</td>    </tr>    <tr>      <th>O</th>      <td>174</td>      <td>166</td>      <td>0.95</td>      <td>58</td>      <td>43</td>      <td>0.74</td>    </tr>    <tr>      <th>P</th>      <td>78</td>      <td>76</td>      <td>0.97</td>      <td>26</td>      <td>18</td>      <td>0.69</td>    </tr>    <tr>      <th>Q</th>      <td>12</td>      <td>12</td>      <td>1.00</td>      <td>4</td>      <td>0</td>      <td>0.00</td>    </tr>    <tr>      <th>R</th>      <td>185</td>      <td>176</td>      <td>0.95</td>      <td>62</td>      <td>38</td>      <td>0.61</td>    </tr>    <tr>      <th>S</th>      <td>162</td>      <td>159</td>      <td>0.98</td>      <td>54</td>      <td>42</td>      <td>0.78</td>    </tr>    <tr>      <th>T</th>      <td>154</td>      <td>151</td>      <td>0.98</td>      <td>51</td>      <td>43</td>      <td>0.84</td>    </tr>    <tr>      <th>U</th>      <td>49</td>      <td>46</td>      <td>0.94</td>      <td>17</td>      <td>12</td>      <td>0.71</td>    </tr>    <tr>      <th>V</th>      <td>38</td>      <td>35</td>      <td>0.92</td>      <td>13</td>      <td>7</td>      <td>0.54</td>    </tr>    <tr>      <th>W</th>      <td>34</td>      <td>31</td>      <td>0.91</td>      <td>11</td>      <td>6</td>      <td>0.55</td>    </tr>    <tr>      <th>X</th>      <td>25</td>      <td>21</td>      <td>0.84</td>      <td>9</td>      <td>4</td>      <td>0.44</td>    </tr>    <tr>      <th>Y</th>      <td>32</td>      <td>27</td>      <td>0.84</td>      <td>11</td>      <td>6</td>      <td>0.55</td>    </tr>    <tr>      <th>Z</th>      <td>18</td>      <td>14</td>      <td>0.78</td>      <td>6</td>      <td>0</td>      <td>0.00</td>    </tr>  </tbody></table>  

#### Accurate Validation Prediction - Sample Images 
![](model4_correct.png)  

#### Inaccurate Validation Prediction - Sample Images 
![](model4_incorrect.png)
