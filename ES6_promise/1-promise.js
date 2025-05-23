/* eslint-disable object-curly-newline,brace-style */
export default function getFullResponseAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({
        status: 200,
        body: 'Success',
      });
    }
    else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
