# frozen_string_literal: true

require 'open3'
require 'fileutils'

# Delete runner.
class DeleteRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    FileUtils.rm_rf(File.expand_path('~/real_log'))
    puts 'Deleted, home directory real_log folder.'
  end
end

begin
  DeleteRunner.run
rescue StandardError => e
  puts e.backtrace
ensure
  GC.compact
end

__END__
