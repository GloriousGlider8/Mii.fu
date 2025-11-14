# Generated automatically with "fut". Do not edit.
import array
import enum
import math

class ZlibImpl:
	"""ZLib compression implementation.

	Must be overrided using a library for your target language!"""

	@staticmethod
	def decompress(input: bytearray | bytes, output: bytearray | bytes, window_bits: int, original_size: int) -> None:
		"""Write the decompressed contents of `input` into `output`.

		`windowBits` and `originalSize` must also be specified."""
		print("!! DEFAULT ZlibImpl DOES NOT DO ANYTHING !!")
		assert False, "You're still using the default ZlibImpl, please override it!"

	@staticmethod
	def compress(input: bytearray | bytes, output: bytearray | bytes, level: int, window_bits: int) -> None:
		"""Write the Compressed contents of `input` into `output`.

		`level` and `windowBits` must also be specified."""
		print("!! DEFAULT ZlibImpl DOES NOT DO ANYTHING !!")
		assert False, "You're still using the default ZlibImpl, please override it!"

class FFLiTextureFormat(enum.Enum):
	GREYSCALE = 0
	GREYSCALE_ALPHA = 1
	R_G_B_A = 2

class FFLiResourceShapeElementType(enum.Enum):
	"""The index that each shape element is stored at.

	Exmaple: `data[FFLiResourceShapeElementType.Position.ToInt()]` would get vertex position data."""
	POSITION = 0
	NORMAL = 1
	TEXCOORD = 2
	TANGENT = 3
	COLOR = 4
	INDEX = 5
	TRANSFORM_HAIR = 6
	TRANSFORM_FACELINE = 7
	BOUNDING_BOX = 8

class Vec3:

	def __init__(self):
		self.x = math.nan
		self.y = math.nan
		self.z = math.nan
	x: float
	y: float
	z: float

	def from_byte_reader(self, data: "ByteReader") -> None:
		"""Reads 3 IEEE 754 4-byte floats into `x`, `y` and `z` respectively."""
		self.x = data.read_float()
		self.y = data.read_float()
		self.z = data.read_float()

	def set_na_n(self) -> None:
		"""Convenience function to set `x`, `y` and `z` to `Math.NaN`."""
		self.x = math.nan
		self.y = math.nan
		self.z = math.nan

class BoundingBox:
	"""Represents the minimum and maximum values of vertex positions in shapes."""

	def __init__(self):
		self.min = Vec3()
		self.max = Vec3()
	min: Vec3
	max: Vec3

	def from_byte_reader(self, data: "ByteReader") -> None:
		"""Reads 2 `Vec3`s into `min` and `max` respectively."""
		self.min.from_byte_reader(data)
		self.max.from_byte_reader(data)

	def set_na_n(self) -> None:
		"""Convenience function to set the `x`, `y` and `z` values of `min` and `max` to `Math.NaN`."""
		self.min.set_na_n()
		self.max.set_na_n()

class WindowBitConverter:
	"""Convenience class containing 1 function to convert `FFLiResourcePartsInfo.WindowBits` to ZLib `windowBits`."""

	@staticmethod
	def f_f_li_resource_window_bits_to_zlib_window_bits(window_bits: int) -> int:
		"""Converts `FFLiResourcePartsInfo.WindowBits` to ZLib `windowBits`."""
		if window_bits <= 7:
			return window_bits + 8
		if window_bits >= 8 and window_bits <= 15:
			return window_bits + 16
		if window_bits == 16:
			return 47
		return 15

class FFLiResourceLoaderObjects:
	"""Passed to `FFLResource.FromByteReader` to provide more options for memory-management."""

	def __init__(self):
		self.texture_beard = [ None ] * 3
		self.texture_cap = [ None ] * 132
		self.texture_eye = [ None ] * 62
		self.texture_eyebrow = [ None ] * 24
		self.texture_wrinkle = [ None ] * 12
		self.texture_makeup = [ None ] * 12
		self.texture_glass = [ None ] * 9
		self.texture_mole = [ None ] * 2
		self.texture_mouth = [ None ] * 37
		self.texture_mustache = [ None ] * 6
		self.texture_noseline = [ None ] * 18
		self.shape_beard = [ None ] * 4
		self.shape_cap_normal = [ None ] * 132
		self.shape_cap_hat = [ None ] * 132
		self.shape_faceline = [ None ] * 12
		self.shape_glass = [ None ] * 1
		self.shape_mask = [ None ] * 12
		self.shape_noseline = [ None ] * 18
		self.shape_nose = [ None ] * 18
		self.shape_hair_normal = [ None ] * 132
		self.shape_hair_hat = [ None ] * 132
		self.shape_forehead_normal = [ None ] * 132
		self.shape_forehead_hat = [ None ] * 132
	resource_header: "FFLiResourceHeader"
	texture_header: "FFLiResourceTextureHeader"
	shape_header: "FFLiResourceShapeHeader"
	texture_beard: list["FFLiResourcePartsInfo | None"]
	texture_cap: list["FFLiResourcePartsInfo | None"]
	texture_eye: list["FFLiResourcePartsInfo | None"]
	texture_eyebrow: list["FFLiResourcePartsInfo | None"]
	texture_wrinkle: list["FFLiResourcePartsInfo | None"]
	texture_makeup: list["FFLiResourcePartsInfo | None"]
	texture_glass: list["FFLiResourcePartsInfo | None"]
	texture_mole: list["FFLiResourcePartsInfo | None"]
	texture_mouth: list["FFLiResourcePartsInfo | None"]
	texture_mustache: list["FFLiResourcePartsInfo | None"]
	texture_noseline: list["FFLiResourcePartsInfo | None"]
	shape_beard: list["FFLiResourcePartsInfo | None"]
	shape_cap_normal: list["FFLiResourcePartsInfo | None"]
	shape_cap_hat: list["FFLiResourcePartsInfo | None"]
	shape_faceline: list["FFLiResourcePartsInfo | None"]
	shape_glass: list["FFLiResourcePartsInfo | None"]
	shape_mask: list["FFLiResourcePartsInfo | None"]
	shape_noseline: list["FFLiResourcePartsInfo | None"]
	shape_nose: list["FFLiResourcePartsInfo | None"]
	shape_hair_normal: list["FFLiResourcePartsInfo | None"]
	shape_hair_hat: list["FFLiResourcePartsInfo | None"]
	shape_forehead_normal: list["FFLiResourcePartsInfo | None"]
	shape_forehead_hat: list["FFLiResourcePartsInfo | None"]

class FFLiPartData:

	def __init__(self):
		self.used = False
	used: bool
	header: "FFLiPartDataHeader"
	footer: "FFLiPartDataFooter"
	data: list[bytearray]

	def from_byte_reader(self, b_utils: "ByteReader", size: int) -> None:
		for i in range(6):
			if self.header.element_size[i] <= 20000000 and self.header.element_size[i] > 0:
				b_utils.seek(self.header.element_offset[i])
				b_utils.read_raw(self.header.element_size[i], self.data[i])
		a: bool = True
		for i in self.header.element_size:
			if i <= 20000000 and i > 0:
				a = False
		if a:
			self.set_unused()
			return
		b_utils.seek(size - 16)
		self.footer.from_byte_reader(b_utils)

	def load_header(self, data: bytearray) -> "ByteReader":
		b_utils: "ByteReader" = ByteReader()
		b_utils.data = data
		self.header.from_byte_reader(b_utils)
		self.used = True
		return b_utils

	def set_unused(self) -> None:
		self.used = False
		self.header.set_unused()

class FFLiPartDataHeader:

	def __init__(self):
		self.element_offset = array.array("i", [ 0 ]) * 6
		self.element_size = array.array("i", [ 0 ]) * 6
		self.bounding_box = BoundingBox()
		self.transform = [ Vec3() for _ in range(6) ]
	element_offset: array.array
	element_size: array.array
	bounding_box: BoundingBox
	transform: list[Vec3]

	def from_byte_reader(self, b_utils: "ByteReader") -> None:
		for i in range(6):
			self.element_offset[i] = b_utils.read_s_int(4)
		for i in range(6):
			self.element_size[i] = b_utils.read_s_int(4)
		if self.element_size[FFLiResourceShapeElementType.INDEX.value] < 20000000:
			self.element_size[FFLiResourceShapeElementType.INDEX.value] *= 2
		self.bounding_box.from_byte_reader(b_utils)
		for i in range(6):
			self.transform[i].from_byte_reader(b_utils)

	def set_unused(self) -> None:
		self.bounding_box.set_na_n()

class FFLiPartDataFooter:
	mip_offset: int
	width: int
	height: int
	format: FFLiTextureFormat
	mip_count: int

	def from_byte_reader(self, data: "ByteReader") -> None:
		self.mip_offset = data.read_u_int(4)
		self.width = data.read_u_short(2)
		self.height = data.read_u_short(2)
		t: int = data.read_byte()
		if t < 3:
			self.format = FFLiTextureFormat(t)
		self.mip_count = data.read_byte()
		data.padding(2)

class FFLiResourcePartsInfo:

	def __init__(self):
		self._b_reader = ByteReader()
	offset: int
	uncompressed_size: int
	compressed_size: int
	compression_level: int
	window_bits: int
	memory_level: int
	strategy: int
	part_data: FFLiPartData
	_b_reader: "ByteReader"

	def from_byte_reader(self, data: "ByteReader", objects: FFLiResourceLoaderObjects) -> None:
		self.offset = data.read_u_int(4)
		self.uncompressed_size = data.read_u_int(4)
		assert self.uncompressed_size < 20000000 and self.uncompressed_size % 2 == 0, "Uncompressed Size invalid (should pass UncompressedSize < 20000000 and (UncompressedSize % 2) == 0)"
		self.compressed_size = data.read_u_int(4)
		assert self.compressed_size <= 20000000, "Compressed Size too large (should be <= 20000000)"
		self.compression_level = data.read_byte()
		assert self.uncompressed_size == 0 or self.compression_level < 11, "Compression Level invalid (should pass UncompressedSize == 0 or CompressionLevel < 11)"
		self.window_bits = data.read_byte()
		self.memory_level = data.read_byte()
		assert self.uncompressed_size == 0 or self.memory_level < 9, "Memory Level invalid (should pass UncompressedSize == 0 or MemoryLevel < 9)"
		self.strategy = data.read_byte()
		assert self.strategy <= 6, "Strategy too large (should be <= 6)"

	def load_header(self, data: "ByteReader", data_buffer: bytearray, compressed_buffer: bytearray) -> None:
		if self.uncompressed_size == 0:
			self.part_data.set_unused()
			return
		o_offset: int = data._offset
		data.seek(self.offset)
		if self.strategy == 5:
			data.read_raw(self.compressed_size, data_buffer)
			self._b_reader = self.part_data.load_header(data_buffer)
			data.seek(o_offset)
			return
		data.read_raw(self.compressed_size, compressed_buffer)
		ZlibImpl.decompress(compressed_buffer, data_buffer, WindowBitConverter.f_f_li_resource_window_bits_to_zlib_window_bits(self.window_bits), self.uncompressed_size)
		self._b_reader = self.part_data.load_header(data_buffer)
		data.seek(o_offset)

	def load_part(self) -> None:
		if self.part_data.used:
			self.part_data.from_byte_reader(self._b_reader, self.uncompressed_size)

class FFLiResourceHeader:
	uncompressed_buffer_size: int
	expanded_buffer_size: int
	is_expand: bool

	def from_byte_reader(self, data: "ByteReader", objects: FFLiResourceLoaderObjects) -> None:
		assert data.read_u_t_f8(4) == "FFRA", "Magic Header invalid (should be FFRA)"
		assert data.read_u_int(4) == 458752, "Version invalid (should be 0x00070000)"
		self.uncompressed_buffer_size = data.read_u_int(4)
		assert self.uncompressed_buffer_size >= 1024, "Uncompressed Buffer Size too small (should be >=1024)"
		self.expanded_buffer_size = data.read_u_int(4)
		assert self.expanded_buffer_size >= 1, "Expanded Buffer Size too small (should be >=1)"
		self.is_expand = data.read_u_int(4) == 1

class FFLiResourceTextureHeader:

	def __init__(self):
		self.texture_max_size = array.array("i", [ 0 ]) * 11
	texture_max_size: array.array

	def from_byte_reader(self, data: "ByteReader", objects: FFLiResourceLoaderObjects) -> None:
		for i in range(11):
			self.texture_max_size[i] = data.read_u_int(4)
			assert self.texture_max_size[i] < 20000000 and self.texture_max_size[i] % 4 == 0, "Texture Max Size invalid (should pass TextureMaxSize < 20000000 and (TextureMaxSize % 4) == 0)"
		for i in range(3):
			objects.texture_beard[i].from_byte_reader(data, objects)
		for i in range(132):
			objects.texture_cap[i].from_byte_reader(data, objects)
		for i in range(62):
			objects.texture_eye[i].from_byte_reader(data, objects)
		for i in range(24):
			objects.texture_eyebrow[i].from_byte_reader(data, objects)
		for i in range(12):
			objects.texture_wrinkle[i].from_byte_reader(data, objects)
		for i in range(12):
			objects.texture_makeup[i].from_byte_reader(data, objects)
		for i in range(9):
			objects.texture_glass[i].from_byte_reader(data, objects)
		for i in range(2):
			objects.texture_mole[i].from_byte_reader(data, objects)
		for i in range(37):
			objects.texture_mouth[i].from_byte_reader(data, objects)
		for i in range(6):
			objects.texture_mustache[i].from_byte_reader(data, objects)
		for i in range(18):
			objects.texture_noseline[i].from_byte_reader(data, objects)

class FFLiResourceShapeHeader:

	def __init__(self):
		self.shape_max_size = array.array("i", [ 0 ]) * 12
	shape_max_size: array.array

	def from_byte_reader(self, data: "ByteReader", objects: FFLiResourceLoaderObjects) -> None:
		for i in range(12):
			self.shape_max_size[i] = data.read_u_int(4)
			assert self.shape_max_size[i] < 20000000 and self.shape_max_size[i] % 2 == 0, "Shape Max Size invalid (should pass ShapeMaxSize < 20000000 and (ShapeMaxSize % 2) == 0)"
		for i in range(4):
			objects.shape_beard[i].from_byte_reader(data, objects)
		for i in range(132):
			objects.shape_cap_normal[i].from_byte_reader(data, objects)
		for i in range(132):
			objects.shape_cap_hat[i].from_byte_reader(data, objects)
		for i in range(12):
			objects.shape_faceline[i].from_byte_reader(data, objects)
		for i in range(1):
			objects.shape_glass[i].from_byte_reader(data, objects)
		for i in range(12):
			objects.shape_mask[i].from_byte_reader(data, objects)
		for i in range(18):
			objects.shape_noseline[i].from_byte_reader(data, objects)
		for i in range(18):
			objects.shape_nose[i].from_byte_reader(data, objects)
		for i in range(132):
			objects.shape_hair_normal[i].from_byte_reader(data, objects)
		for i in range(132):
			objects.shape_hair_hat[i].from_byte_reader(data, objects)
		for i in range(132):
			objects.shape_forehead_normal[i].from_byte_reader(data, objects)
		for i in range(132):
			objects.shape_forehead_hat[i].from_byte_reader(data, objects)

class FFLResource:
	"""## FFLResource
	`FFLResource` is used for the loading of FFL / AFL Resource files.

	### Loading a Resource
	Use `FFLResource.FromByteReader` to load a resource from a `ByteReader`, storing objects in a `FFLiResourceLoaderObjects` object."""

	def __init__(self):
		self.is_loaded = False
		self.is_a_f_l23 = False
		self.is_a_f_l = False
	is_loaded: bool
	is_a_f_l23: bool
	is_a_f_l: bool

	def from_byte_reader(self, data: "ByteReader", objects: FFLiResourceLoaderObjects) -> None:
		"""Loads a resource from a `ByteReader`, storing objects in a `FFLiResourceLoaderObjects` object."""
		objects.resource_header.from_byte_reader(data, objects)
		self.is_a_f_l23 = objects.resource_header.expanded_buffer_size == 38809056
		self.is_a_f_l = self.is_a_f_l23 or objects.resource_header.expanded_buffer_size == 37344736
		objects.texture_header.from_byte_reader(data, objects)
		objects.shape_header.from_byte_reader(data, objects)
		self.is_loaded = True

class BitConverter:

	@staticmethod
	def convert1010102_to_float(packed: int, out_vec: array.array, offset: int) -> None:
		"""Converts packed 10_10_10_2 SNORM (signed normalized) to float[3]"""
		nx: int = packed << 22 >> 22
		ny: int = packed << 12 >> 22
		nz: int = packed << 2 >> 22
		out_vec[offset * 3 + 0] = nx / 511.0
		out_vec[offset * 3 + 1] = ny / 511.0
		out_vec[offset * 3 + 2] = nz / 511.0

	@staticmethod
	def convert8888_snorm_to_float(packed: int, out_vec: array.array) -> None:
		"""Converts packed 8_8_8_8 SNORM (signed normalized) to float[4]"""
		r: int = packed >> 16 & 255
		g: int = packed >> 8 & 255
		b: int = packed & 255
		a: int = packed >> 24 & 255
		if r > 127:
			r -= 256
		if g > 127:
			g -= 256
		if b > 127:
			b -= 256
		if a > 127:
			a -= 256
		out_vec[0] = r / 127.0
		out_vec[1] = g / 127.0
		out_vec[2] = b / 127.0
		out_vec[3] = a / 127.0

	@staticmethod
	def half_to_float(half: int) -> float:
		"""Converts 16-bit half-float to 32-bit float (IEEE754)"""
		sign: int = half >> 15 & 1
		exp: int = half >> 10 & 31
		mant: int = half & 1023
		if exp == 0:
			if mant == 0:
				f = sign << 31
			else:
				exp = 1
				while (mant & 1024) == 0:
					mant <<= 1
					exp -= 1
				mant &= 1023
				exp += 112
				f = sign << 31 | exp << 23 | mant << 13
		elif exp == 31:
			f = sign << 31 | 2139095040 | mant << 13
		else:
			add: int = 112
			exp = exp + add
			f = sign << 31 | exp << 23 | mant << 13
		return BitConverter.u_int_to_float(f)

	@staticmethod
	def u_int_to_float(bits: int) -> float:
		"""Convert 32-bit unsigned integer to floating point.

		As of 3.2.10, Fusion does not include any method to
		convert bits to float, so native implementations are provided
		along with a generic slow and terrible but functional fallback."""
		sign: bool = (bits & 2147483648) != 0
		exp: int = bits >> 23 & 255
		frac: int = bits & 8388607
		if exp == 0:
			if frac == 0:
				return -0.0 if sign else 0.0
			mantissa = frac / math.pow(2.0, 23)
			value = math.pow(2.0, -126) * mantissa
		elif exp == 255:
			if frac != 0:
				return math.nan
			return -math.inf if sign else math.inf
		else:
			mantissa = 1.0 + frac / math.pow(2.0, 23)
			value = mantissa * math.pow(2.0, exp - 127)
		return -value if sign else value

	@staticmethod
	def float_to_int(v: float) -> int:
		assert False, "Not implemented for pure Fusion."

class BitfieldReader:
	"""Convenience class to read values from bitfields"""
	value: int
	_offset: int

	def seek(self, where: int) -> None:
		"""Move the bit pointer to `where` bits"""
		self._offset = where

	def padding(self, size: int) -> None:
		"""Move the bit pointer ahead by `size` bit
		This is prefered in place of `Seek`"""
		self._offset += size

	def read_bool(self) -> bool:
		"""Reads 1 bit and returns it as a `bool`"""
		result = (self.value & 1 << self._offset) != 0
		self._offset += 1
		return result

	def read_bits(self, size: int) -> int:
		"""Reads `size` bits into a `byte`"""
		result: int = 0
		for i in range(size):
			bit: int = self.value >> self._offset & 1
			self._offset += 1
			result |= bit << i
		return result

class ByteReader:
	"""Convenience class to read values from bytes.

	All methods assume big-endian byte order."""

	def __init__(self):
		self._offset = 0
	data: bytearray
	_offset: int

	def seek(self, where: int) -> None:
		"""Move the file pointer to `where` bytes."""
		self._offset = where

	def padding(self, size: int) -> None:
		"""Move the file pointer ahead by `size` bytes.

		This is prefered in place of `Seek`."""
		self._offset += size

	def read_byte(self) -> int:
		"""Reads 1 byte into a `byte`.

		Range: `0 .. 255`."""
		result = self.data[self._offset]
		self._offset += 1
		return result

	def read_u_short(self, size: int) -> int:
		"""Reads `size` bytes and stores them in a `ushort`.

		Range: `0 .. 65535`."""
		res: int = 0
		for _ in range(size):
			res = res << 8 | self.data[self._offset]
			self._offset += 1
		return res

	def read_u_int(self, size: int) -> int:
		"""Reads `size` bytes and stores them in a `uint`.

		Range: `0 .. 2147483647`."""
		res: int = 0
		for _ in range(size):
			res = res << 8 | self.data[self._offset]
			self._offset += 1
		return res

	def read_s_short(self, size: int) -> int:
		"""Reads `size` bytes and stores them in a `short`.

		Range: `-32768 .. 32767`."""
		res: int = 0
		for _ in range(size):
			res = res << 8 | self.data[self._offset]
			self._offset += 1
		sign_bit: int = 1 << (size * 8 - 1)
		if (res & sign_bit) != 0:
			res -= 1 << size * 8
		return res

	def read_s_int(self, size: int) -> int:
		"""Reads `size` bytes and stores them in an `int`.

		Range: `-2147483648 .. 2147483647`."""
		res: int = 0
		for _ in range(size):
			res = res << 8 | self.data[self._offset]
			self._offset += 1
		sign_bit: int = 1 << (size * 8 - 1)
		if (res & sign_bit) != 0:
			res -= 1 << size * 8
		return res

	def read_s_long(self, size: int) -> int:
		"""Reads `size` bytes and stores them in a `long`.

		Range `-9223372036854775808 .. 9223372036854775807`."""
		res: int = 0
		for _ in range(size):
			res = res << 8 | self.data[self._offset]
			self._offset += 1
		sign_bit: int = 1 << (size * 8 - 1)
		if (res & sign_bit) != 0:
			res -= 1 << size * 8
		return res

	def get_bitfield(self) -> BitfieldReader:
		"""Reads 1 byte into a `BitfieldReader`.

		This serves as a convenience method and still advances the pointer."""
		b: BitfieldReader = BitfieldReader()
		b.value = self.data[self._offset]
		self._offset += 1
		return b

	def read_float(self) -> float:
		"""Reads 4 bytes and stores them in a `float`.

		Uses the IEEE 754 format."""
		raw: int = self.read_u_int(4)
		return BitConverter.u_int_to_float(raw)

	def read_u_t_f8(self, size: int) -> str:
		"""Reads `size` bytes and interprets them as a UTF8 string."""
		self._offset += size
		return self.data[self._offset - size:self._offset - size + size].decode("utf8")

	def read_raw(self, size: int, buffer: bytearray) -> None:
		"""Reads `size` bytes and stores them in `buffer`."""
		buffer[0:size] = self.data[self._offset:self._offset + size]
		self._offset += size
