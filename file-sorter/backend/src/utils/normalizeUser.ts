import { User } from "../types/user";

function safeString(value: any): string {
    if (!value) return "";
    return String(value).trim();
}

function safeNumber(value: any): number {
    const parsed = Number(value);
    if (Number.isNaN(parsed)) return 0;
    return parsed;
}

export function normalizeUser(item: any): User {
    return {
        id: safeNumber(item.ID || item.id),

        firstName: safeString(item.firstName),
        middleName: safeString(item.middleName),

        firstLastName:
            safeString(item.firstLastName) ||
            safeString(item.lastName1) ||
            safeString(item.apellido1),

        secondLastName:
            safeString(item.secondLastName) ||
            safeString(item.lastName2) ||
            safeString(item.apellido2),

        phoneNumber: safeString(item.phoneNumber),
        address: safeString(item.address)
    };
}