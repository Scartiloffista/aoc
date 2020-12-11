file = File.open(__dir__ + "/../inputs/1.txt").read.
lines = file.split("\n").map(&:to_i).

lines.permutation(3).each do |a, b, c|
    if a+b+c == 2020
        puts (a*b*c)
    end
end