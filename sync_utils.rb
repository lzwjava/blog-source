class SyncUtils
    def self.mkdir!(dir)
        if Dir.exists?(dir)
            FileUtils.rm_r(dir)
        end
        Dir.mkdir(dir)
    end

    def self.extract_title(content)
        title = content.lines.first
        if title.include? '##'
            title = title[title.index('##') + 2..-1]
        elsif title.include? '#'
            title = title[title.index('#') + 1..-1]
        end
        return title.strip        
    end

    def post_front(title)
        return "---\n" \
        "layout: post\n" \
        "title:  \"#{title}\"\n" \
        "---\n"
    end
end