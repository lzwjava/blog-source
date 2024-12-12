source "https://rubygems.org"

# Specify the Jekyll version
gem 'jekyll', '~> 3.9.3'

# Default theme for new Jekyll sites
gem 'minima', '~> 2.5'

# GitHub Pages plugin
group :jekyll_plugins do
  gem 'github-pages', '~> 228'
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?

# Additional plugins
gem 'jekyll-sitemap', '~> 1.4'
gem 'jekyll-seo-tag', '~> 2.8'
gem 'webrick', '~> 1.7'

# Ensure compatibility with the logger gem
gem 'logger', '~> 1.5.3'

# Ensure compatibility with the rubyzip gem
gem 'rubyzip', '~> 2.3.0'
