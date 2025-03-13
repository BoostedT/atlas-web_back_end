/* eslint-disable import/extensions */
import { uploadPhoto } from "./utils.js";
import { createUser } from "./utils.js";

export async function handleProfileSignup() {
  const photo = await uploadPhoto();
  const user = await createUser();

  console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  return { photo, user };
} 
