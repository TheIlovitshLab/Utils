/*
 * Batch convert 16-bit tiffs in input ffolder to 8-bit tiffs with same name in output folder
 */

#@ File (label = "Input directory", style = "directory") input
#@ File (label = "Output directory", style = "directory") output
#@ String (label = "File suffix", value = ".tif") suffix

// See also Process_Folder.py for a version of this code
// in the Python scripting language.

processFolder(input);

// function to scan folders/subfolders/files to find files with correct suffix
function processFolder(input) {
	list = getFileList(input);
	list = Array.sort(list);
	for (i = 0; i < list.length; i++) {
		if(File.isDirectory(input + File.separator + list[i]))
			processFolder(input + File.separator + list[i]);
		if(endsWith(list[i], suffix))
			processFile(input, output, list[i]);
	}
	print("finished")
}

function processFile(input, output, file) {
	print("Processing: " + input + File.separator + file);
	funstr = "open="+"["+ input + File.separator + file + "]" + " color_mode=Composite rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT" ;
	run("Bio-Formats",funstr);
	run("8-bit");
	print("Saving to: " + output);
	saveAs("Tiff", output + File.separator + file);
	close();
}
