function rename_multiple(old_str,new_str,path)
if nargin<3
    path = uigetdir('Choose folder');
end
old_names = dir(fullfile(path));
for i = 1:length(old_names)
    old_file = old_names(i);
    old_name = fullfile(old_file.folder,old_file.name);
    if strfind(old_name,old_str)~=-1
        new_name = fullfile(old_file.folder,strrep(old_file.name,old_str,new_str));
        movefile(old_name,new_name,'f');
    end
end
end