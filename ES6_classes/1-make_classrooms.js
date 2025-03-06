  /* eslint-disable-next-line import/extensions */
import Classroom from './0-classroom.js';

  /* eslint-disable-next-line no-multiple-empty-lines */
export default function initializeRooms() {
  const rooms = [
    new Classroom(19),
    new Classroom(20),
    new Classroom(34),
  ];

  return rooms;
}
