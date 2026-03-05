import { Router } from "express";
import multer from "multer";
import { uploadAndSort } from "../controllers/file.controller";

const router = Router();

const upload = multer({
    storage: multer.memoryStorage(),
    limits: {
        fileSize: 5 * 1024 * 1024, // 5MB
    },
});

router.post("/upload", upload.single("file"), uploadAndSort);

export default router;
