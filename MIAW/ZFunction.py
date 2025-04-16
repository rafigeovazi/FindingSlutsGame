#abs(x): mengembalikan nilai absolut dari 'x'
abs(-5) #Outputnya: 5
#all(iterable): mengembalikan True jika semua elemen dalam 'iterable' adalah benar
all([True, True, False]) #Output: False
#any(iterable): mengembalikan True jika salah satu elemen dalam 'iterable' adalah benar
any([False, False, True]) #Output: True
#ascii(object): mengembalikan representasi string dari objek, dengan karakter non-ASCII digantikan oleh urutan escape
ascii('äöü') #Output: "'\\xe4\\xf6\\xfc'"
#bin(x): mengembalikan representasi biner dari bilangan bulat 'x'
bin(10) #Output: '0b1010' = bilangan biner dari 10
#bool([x]): mengonversi nilai menjadi boolean, yaitu hanya True dan False
bool(1) #Output: True = karena nilai True dalam biner adalah 1
#bytearray([source[, encoding[, errors]]]): mengembalikan objek bytearray
bytearray('hello', 'utf-8') #Output: bytearray(b'hello')
#bytes([source[, encoding[, errors]]])': mengembalikan objek 'bytes'
bytes('hello', 'utf-8') #Output: b'hello'
#callable(object): mengembalikan True jika objek dapat dipanggil
callable(print) #Output: True
#chr(i): mengembalikan karakter sting yng mewakili kode Unicode 'i'
chr(97) #Output: 'a' = dalam karakter dari unicode 97 adalah huruf kecil latin a
#classmethod(function): mengoversi metode menjadi metode kelas
class MyClass:
    @classmethod
    def my_classmethod(cls):
        pass
#compile(source, filename, mode): mengompilasi sumber kode ke dalam kode byte python
code = compile('print("Hell World!")', '<string>', 'exec')
exec(code)
#complex([real[, image]]): mengembalikan bilangan kompleks
complex(1, 2) #Output: (1+2j)
#delattr(object, name): menghapus atribut bernama dari objek
class MyClass:
    pass
obj = MyClass()
obj.attribute = 'value'
delattr(obj, 'attribute')
#dict([arg]): mengembalikan objek dictionary baru
dict(a=1, b=2) #Output: {'a': 1, 'b': 2}
#dir([object]): mengembalikan daftar atribut valid dari objek
dir([]) #Output: ['append', 'clear', 'copy', ....]
#divmod(a, b): mengembalikan pasangan (a // b, a % b)
divmod(7,3) #Output: (2, 1)
#enumerate(iterable, start=0): mengembalikan objek enumerate
list(enumerate(['a', 'b', 'c'])) #Output: [(0, 'a'), (1, 'b'), (2, 'c')]
#eval(expression[, globals[, locals]]): mengevaluasi ekspresi dalam string sebagai kode python
eval('1 + 2')  # Output: 3
#exec(object[, globals[, locals]]): menjalankan objek kode python
exec('print("Hello, World!")')
#filter(function, iterable): menyaring elemen dari iterable yang memenuhi fungsi function
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # Output: [1, 2]
#float([x]): mengonversi nilai menjadi bilangan titik mengambang
float('1.23')  # Output: 1.23
#format(value[, format_spec]): memformat nilai sesuai dengan spesifikasi format
format(3.14159, '.2f')  # Output: '3.14'
#frozenset([iterable]): mengembalikan objek set yang tidak dapat diubah
frozenset([1, 2, 3])  # Output: frozenset({1, 2, 3})
#getattr(object, name[, default]): mengembalikan nilai atribut bernama dari objek
class MyClass:
    attribute = 'value'
obj = MyClass()
getattr(obj, 'attribute')  # Output: 'value'
#globals(): mengembalikan kamus dari simbol global saat ini
globals()
#hasattr(object, name): mengembalikan True jika objek memiliki atribut bernama
class MyClass:
    attribute = 'value'
obj = MyClass()
hasattr(obj, 'attribute')  # Output: True
#hash(object): mengembalikan nilai hash dari objek jika memiliki nilai hash
hash('test')  # Output: hash value of 'test'
#help([object]): menampilkan bantuan untuk objek
help(print)
#hex(x): mengembalikan representasi heksadesimal dari bilangan bulat x
hex(255)  # Output: '0xff'
#id(object): mengembalikan nilai identitas dari objek
id(42)  # Output: identity of 42
#input([prompt]): membaca string dari input pengguna
name = input('Enter your name: ')
#int([x[, base]]): mengonversi nilai menjadi bilangan bulat
int('10')  # Output: 10
#isinstance(object, classinfo): mengembalikan True jika objek adalah instance dari classinfo
isinstance(5, int)  # Output: True
#issubclass(class, classinfo): mengembalikan True jika class adalah subclass dari classinfo
issubclass(bool, int)  # Output: True
#iter(object[, sentinel]): mengembalikan iterator untuk objek
iter([1, 2, 3])
#len(s): mengembalikan panjang (jumlah item) dari objek
len([1, 2, 3])  # Output: 3
#list([iterable]): mengembalikan daftar dari iterable
list('abc')  # Output: ['a', 'b', 'c']
#locals(): mengembalikan kamus dari simbol lokal saat ini
locals()
#map(function, iterable, ...): menerapkan fungsi ke setiap item dalam iterable
list(map(lambda x: x * 2, [1, 2, 3]))  # Output: [2, 4, 6] 