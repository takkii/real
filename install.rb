# frozen_string_literal: true

require 'open3'
require 'fileutils'

# Installer runner.
class InstallerRunner

  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    if File.exist?('./dict/method.txt')
      puts 'Already, Have a method.txt'
    else
      stdout_rb = Open3.capture3("ruby ./dict/ruby_method.rb")
      stdout_rb
      FileUtils.mv(['./method.txt'], "./dict")
      puts 'Installed, The RubyMethod to a Text File.'
    end
  end
end

# About Exception, begin ~ rescue ~ ensure.
begin
  InstallerRunner.run
rescue StandardError => e
  puts e.backtrace
ensure
  GC.compact
end

__END__
