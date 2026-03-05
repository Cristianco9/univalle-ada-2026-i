import { z } from "zod";

export const userSchema = z.object({
    id: z.number().int().positive(),
    firstName: z.string().min(1),
    middleName: z.string().min(1),
    firstLastName: z.string().min(1),
    secondLastName: z.string().min(1),
    phoneNumber: z.string().min(7),
    address: z.string().min(1)
});