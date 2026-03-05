import { parse } from "csv-parse/sync";

export function parseFile(buffer: Buffer) {
    const content = buffer.toString("utf-8");

    return parse(content, {
        columns: true,
        skip_empty_lines: true,
        trim: true,
        relax_column_count: true,
        relax_quotes: true,
        skip_records_with_error: true
    });
}