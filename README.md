# work-12
Renaming file based on file content at a particular location

## Input
The input task is as follows:
<p align="center">
  <img src="images/work_12_input.png" alt="Work-12 Input" width="" height="">
</p>

* There are multiple files with name as random number.
* There are different parameters in the input file
	- `wafer id`
	- `lot id`
	- `step id`



## Output
The output is as follows:
<p align="center">
  <img src="images/work_12_output.png" alt="Work-12 Output" width="" height="">
</p>

* The random named files will be renamed w.r.t nomenclature as `<lot_id>_<step_id>_<wafer_id>`. E.g: `F19310002.F1_POLY_WF01`
* Also, the file contents of the respective file is changed as shown below:
	- `Lot_ID`
	- `Results_ID`

## Coding
The pseudo code is as follows:

1. Walk in directory 
2. Select the files with (*.001) extension (if available).
3. Take the parameters & modify the content
4. Write it back into the file
5. Also, change the file name

## Demo
The demo video is available [here](./videos/work_12_demo.mp4)