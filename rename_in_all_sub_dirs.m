path = uigetdir();
pattern = '*'; % Change if neccassery
[files,paths] = recdir(path,pattern);
old_str = 'midbrain';
new_str = 'hypothalamus';
for i = 1:length(files)
    old_name = fullfile(paths{i},files{i});
    if strfind(old_name,old_str)~=-1
        new_name = fullfile(paths{i},strrep(files{i},old_str,new_str));
        movefile(old_name,new_name);
    end
end