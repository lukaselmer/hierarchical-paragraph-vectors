require 'csv'

def convert(name, review_column)
  text = File.read("../data/#{name}.tsv").gsub(/\\"/, '""')
  all_lines = CSV.parse(text, col_sep: "\t")
  #aa = a[10][2].encode!("UTF-8")

  all_subs = [
    ['‘', "'"],
    ['´', "'"],
    ['`', "'"],
    ['’', "'"],
    ['“', '"'],
    ['«', '"'],
    ['»', '"'],
  ]

  all_subs += [
    ['®', 'CPYRGHT'],
    ['<em>', 'EM'],
    ['</em>', 'EEM'],
    ['<i>', 'STARTI'],
    ['</i>', 'ENDI'],
    ["'s ", 'APS'],
    [/\t+/, 'TAB'],
  ].map { |v| [v[0], " SPECIALCHAR#{v[1]} "] }

  all_subs += [
    ['<br /><br />', 'DBR'],
    ['<br />', 'BR'],
    ['<hr>', 'HR'],
  ].map { |v| [v[0], " PARAGRAPHEND SPECIALPARACHAR#{v[1]} "] }

  all_subs += [':-)', ':-p', ':-P', ':-(', ':-D', '</3', '<3', '<=8'].each_with_index.map do |x, i|
    [x, " SPECIALCHARSMILEY#{i} "]
  end

  # xxxx--yyyy
  # replace X.Y.
  # numbera/numberb
  # (?????)
  # ?!?!
  # letter*****letter****letter
  # many ...
  # many !!!
  # many ???
  # many $$$
  # many ---
  # many *** (including count!)
  all_subs += [
    [/([a-z0-9])--+([a-z0-9])/i, '\1 SPECIAL \2'],
    [/([a-z0-9])\.([a-z0-9])\./i, ' \1\2SPECIAL '],
    [/([a-z0-9])\.([a-z0-9])\./i, ' \1\2SPECIAL '],
    [/([0-9])\/([0-9][0-9]?)/i, ' \1SPECIAL\2 '],
    [/([a-z]\*\*+)([a-z]\*\*+)?([a-z]\*\*+)?[a-z]?/i, ' SPECIAL '],
    [/(\!|\?)*(\!\?|\?\!)(\!|\?)*/i, ' SPECIAL SENTENCEEND '],
    [/\(\?+\)/i, ' SPECIAL SENTENCEEND '],
    [/\.\.+/i, ' SPECIAL SENTENCEEND '],
    [/\!\!+/i, ' SPECIAL SENTENCEEND '],
    [/\$\$+/i, ' SPECIAL '],
    [/\-\-+/i, ' SPECIAL '],
    [/ \*\*\*\*\* /i, ' SPECIAL '],
    [/ \*\*\*\* /i, ' SPECIAL '],
    [/ \*\*\* /i, ' SPECIAL '],
    [/ \*\* /i, ' SPECIAL '],
    [/\*\*+/i, ' SPECIAL '],
    [/#[ ]?([0-9])/i, ' SPECIAL\1 '],
  ].each_with_index.map { |x, i| [x[0], x[1].gsub('SPECIAL', "EXSPEC#{i}")] }

  all_subs += [['₤', '$'], ['£', '$']]
  all_subs += '!.?'.split('').each_with_index.map { |x, i| [x, " SENTSPECL#{i} SENTENCEEND "] }
  all_subs += '),;:'.split('').each_with_index.map { |x, i| [x, " SUBSENTSPECL#{i} SUBSENTENCEEND "] }
  all_subs += '('.split('').each_with_index.map { |x, i| [x, " SUBSENTENCEEND SUBSENTSPECLBRA#{i} "] }
  all_subs += '|~#"\'{}[]+-–°*ç%&/=\\<>_^§$@'.split('').each_with_index.map { |x, i| [x, " SPECSINGL#{i} "] }
  #all_subs += 'êßãåøñíÊùáóäüöëéàè½¨'.split('').map { |x| [x, ''] }
  #all_subs += %W(\u0096 \u0097 \u0091 \u0084).map { |v| [v, ''] }

  all_subs += ([['  ', ' ']] * 10)

  #while line = gets do
  #  all_subs.each do |find, replace|
  #    line = line.gsub(find, replace)
  #  end
  #  puts line
  #end

  i = 0
  updated_lines = all_lines.map do |line|
    i += 1
    if i % 5000 == 0
      puts i
    end

    if false
      new_line = line.dup
      review = new_line[review_column].downcase
      all_subs.each do |find, replace|
        review = review.gsub(find, replace)
      end
      review = review.gsub(/[^0-9a-z ]+/i, '')
    else
      new_line = line.dup
      review = new_line[review_column].downcase
    end

    #extracted = review.scan(/[^0-9a-z ]+/i)
    #if extracted.length > 0
    #  strange += extracted
    #end

    new_line[review_column] = review.strip
    new_line
  end

  #p strange.uniq.sort.join('')

  CSV.open("#{name}Clean.csv", 'w') do |csv|
    updated_lines.each do |new_line|
      csv << new_line
    end
  end
end

convert('labeledTrainData', 2)
convert('testData', 1)
convert('unlabeledTrainData', 1)
