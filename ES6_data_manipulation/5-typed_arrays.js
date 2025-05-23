export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const int8View = new DataView(buffer, 0, length);

  int8View.setInt8(position, value);
  /* eslint-disable semi-spacing */
  return int8View;
}
