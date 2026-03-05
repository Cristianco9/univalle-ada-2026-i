import { Request, Response } from "express";
import { parseFile } from "../utils/parseFile";
import { sortUsers } from "../services/sort.service";
import { normalizeUser } from "../utils/normalizeUser";
import { Parser } from "json2csv";

export async function uploadAndSort(req: Request, res: Response) {
    try {
        if (!req.file) {
            return res.status(400).json({ error: "File is required" });
        }

        const rawData = parseFile(req.file.buffer);

        if (!Array.isArray(rawData) || rawData.length === 0) {
            return res.status(400).json({ error: "Empty or invalid file" });
        }

        // Normalize once (O(n))
        const users = new Array(rawData.length);

        for (let i = 0; i < rawData.length; i++) {
            users[i] = normalizeUser(rawData[i]);
        }

        // Sort once (O(n log n))
        sortUsers(users);

        const parser = new Parser({
            fields: [
                "id",
                "firstName",
                "middleName",
                "firstLastName",
                "secondLastName",
                "phoneNumber",
                "address"
            ]
        });

        const csv = parser.parse(users);

        res.setHeader("Content-Type", "text/csv");
        res.setHeader("Content-Disposition", "attachment; filename=sorted_users.csv");

        return res.status(200).send(csv);

    } catch (error: any) {
        console.error("Processing error:", error);
        return res.status(500).json({
            error: "Internal processing error"
        });
    }
}