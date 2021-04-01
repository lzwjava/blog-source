class SyncUtils
    def self.mkdir!(dir)
        if Dir.exists?(dir)
            FileUtils.rm_r(dir)
        end
        Dir.mkdir(dir)
    end
end