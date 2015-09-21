#!/usr/bin/env ruby

def main
  current_epoch = current_hpv = -1
  File.readlines('big.log').each do |line|
    /Epoch (?<epoch>\d*) of \d*/ =~ line
    current_epoch = epoch if epoch

    /\'hierarchical_paragraph_vectors\'\: (?<hpv>\d*)/ =~ line
    current_hpv = hpv if hpv

    if line.include?('Model training for dm')
      dm = line.include?('dm1') ? 'DM' : 'DBOW'
      /took (?<seconds>\d*\.\d*) seconds/ =~ line
      puts [48, hpv_map[current_hpv.to_i], current_epoch, dm, 'm', seconds].join("\t")
    end
  end
end

def hpv_map
  {
    0 => 'NO-HPV',
    1 => 'HPV-PAR-SENT-SUB',
    3 => 'HPV-PAR-SENT-SUBNV',
    2 => 'HPV-PAR-SENT',
    4 => 'HPV-TOP',
    5 => 'HPV-TOP-PAR-SENT',
    6 => 'HPV-PAR',
    7 => 'HPV-TOP-PAR'
  }
end

main

