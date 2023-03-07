# frozen_string_literal: true

require 'fileutils'

# Installer runner.
class UnInstallerRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    FileUtils.rm_rf(File.expand_path('~/config'))
    stdout_rq, _stderr_rq, _status_rq = Open3.capture3('pip3 uninstall -y -r requirements.txt')
    stdout_rq
  end
end

UnInstallerRunner.run
