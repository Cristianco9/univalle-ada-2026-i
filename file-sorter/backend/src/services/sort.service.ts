import { User } from "../types/user";

function compareString(a: string, b: string): number {
    if (a === b) return 0;
    if (a === "") return 1;   // push empty values last
    if (b === "") return -1;
    return a.localeCompare(b);
}

export function sortUsers(users: User[]): User[] {
    return users.sort((a, b) => {
        return (
            a.id - b.id ||
            compareString(a.firstName, b.firstName) ||
            compareString(a.middleName, b.middleName) ||
            compareString(a.firstLastName, b.firstLastName) ||
            compareString(a.secondLastName, b.secondLastName) ||
            compareString(a.phoneNumber, b.phoneNumber) ||
            compareString(a.address, b.address)
        );
    });
}