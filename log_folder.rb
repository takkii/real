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
    if Dir.exist?(File.expand_path('~/real_log'))
      puts '既に、real_logフォルダがあります...何もしません。'
    else
      FileUtils.mkdir('real_log')
      FileUtils.mv("#{File.dirname(__FILE__)}/real_log", File.expand_path('~/'))
      puts 'real_logフォルダを作成しました。'
    end
  end
end

InstallerRunner.run
