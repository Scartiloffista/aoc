file = File.open(__dir__ + "/../inputs/2.txt").read
lines: String = file.split("\n")

lines.each do |line|
    puts line
end