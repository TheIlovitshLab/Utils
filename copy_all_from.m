function copy_all_from(str)
% Move all files containing str in name to new folder
oldpath = uigetdir('Choose input folder');
new_path = uigetdir('Choose output folder');
old_names = dir(fullfile(oldpath));
for i = 1:length(old_names)
    old_file = old_names(i);
    old_name = fullfile(old_file.folder,old_file.name);
    if strfind(old_name,str)~=-1
        new_name = fullfile(new_path,old_file.name);
        copyfile(old_name,new_name,'f');
    end
end
end