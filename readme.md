# Find Laptop
This software is going to be used primarily for the Serbian/Bosnian region to find the cheapest laptop on the cheapest and also the best laptop in the region. 

It will contain a database of the laptops that are found on the internet and thereby using our **super special algorithm** to create an index of all the laptops, finding the **best one**, as well as the **cheapest one**. 

## Index rank
The base index data points are as follows, every point is using a range from **1** *(worst)* to **3** *(best)* except the CPU *(processor)*

- **Price** - We only support **EURO** as a currency.
- **CPU** - Efficiency is marked from 53 points or more. 
- **Battery** - Condition can range from really bad to usable *(medium)* to good (new/really good)*
- **RAM** - There is no condition for RAM only sizes, going from size 1GB *(worst)* to 2GB *(medium)* to 4GB+ *(best)*
- **Screen Resolutin** - Scale ranges from Under **1366x768** to exactly **1366x768** and also **more** than 1367x768 *(best)   for instance* **1920x1080.** 
- **Screen Quality** - This data point contains if the screen is damaged or has any other problems, one example would be dead pixels. The best case scenario is there are no problems and the screen is perfectly fine.
- **State** - Likewise the other problems and other conditions of the laptop are fit within this one data point where we will express any problems with the laptop or issues, an example would be a dead key, this wouldn't range high but would pose a problem for the buyer if it can not be replaced, sometimes making it unusable.

## Design Proposal

- [Design](https://www.figma.com/file/h1yFFQpggoZzxZ4cm8ujc2/Design?node-id=0%3A1)
