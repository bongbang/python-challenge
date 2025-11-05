shift = 2
alphabets = [chr(x) for x in range(ord('a'), ord('z')+1)]
decoder_table = str.maketrans({alphabets[i-shift]:x for i, x in enumerate(alphabets)})

cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# use doublq quotes b/c string contains '
print(cipher.translate(decoder_table), '\n')
print('map'.translate(decoder_table))
