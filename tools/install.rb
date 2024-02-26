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
    if Dir.exist?(File.expand_path('~/config'))
      stdout_rq, _stderr_rq, _status_rq = Open3.capture3('pip3 install -r requirements.txt')
      stdout_rq
    else
      stdout_gt, _stderr_gt, _status_gt = Open3.capture3('git clone git@github.com:takkii/config.git')
      stdout_gt
      FileUtils.mv("#{File.dirname(__FILE__)}/config", File.expand_path('~/'))
      stdout_rq, _stderr_rq, _status_rq = Open3.capture3('pip3 install -r requirements.txt')
      stdout_rq
    end
  end
end

begin
  InstallerRunner.run
rescue StandardError => e
  puts e.backtrace
ensure
  GC.compact
end

__END__
