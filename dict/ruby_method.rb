#!/usr/bin/ruby

class RubyMethod
  def initialize
    @methods = Class.methods + Object.methods
  end

  def write_to_file
    File.open('methods.txt', 'a:utf-8', perm = 0o777) do |f|
      f.puts @methods.sort.uniq
    end
  end
end

RubyMethod.new.write_to_file
