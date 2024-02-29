# frozen_string_literal: true

require 'open3'
require 'fileutils'

# Create runner.
class CreateRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    if Dir.exist?(File.expand_path('~/real_log'))
      puts 'Already have a real_log folder...do nothing.'
    else
      FileUtils.mkdir('real_log')
      FileUtils.mv("#{File.dirname(__FILE__)}/real_log", File.expand_path('~/'))
      puts 'Created, real_log folder.'
    end
  end
end

begin
  CreateRunner.run
rescue StandardError => e
  puts e.backtrace
ensure
  GC.compact
end

__END__
