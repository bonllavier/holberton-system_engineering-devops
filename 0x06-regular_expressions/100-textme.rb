#!/usr/bin/env ruby
concat = ARGV[0].scan(/\[(?:from):(.*?)\]/).join + ","
concat = concat + ARGV[0].scan(/\[(?:to):(.*?)\]/).join + ","
concat = concat + ARGV[0].scan(/\[(?:flags):(.*?)\]/).join
puts concat
