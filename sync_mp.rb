require 'pathname'
require 'fileutils'
require './sync_utils.rb'

base = '/Users/lzw/ideas/my-essays/blog'
target = Dir.pwd
project = 'mp'
posts_dir = File.join(target, '_posts', project)
img_dir = File.join(target, 'assets', 'images', project)
img_url_base = "/assets/images/#{project}"

SyncUtils.mkdir!(posts_dir)
SyncUtils.mkdir!(img_dir)

Dir.each_child(base) { |x|
    if File.extname(x) == '.md'
        mdfile = File.join(base, x)
        content = File.read(mdfile)
        if content.length == 0
            next
        end
        title = SyncUtils.extract_title(content)

        front = SyncUtils.post_front(title)        

        content = content.lines[1..-1].join

        content = front + content

        file_name = x

        target_file = File.join(posts_dir, file_name)

        origin_img_dir = File.join(base, 'img')
        if Dir.exists?(origin_img_dir)

            FileUtils.cp_r(origin_img_dir + '/.', img_dir)
        end

        img_path = "#{img_url_base}/"

        content = content.gsub('./img/', img_path)

        File.write(target_file, content)
    end
}