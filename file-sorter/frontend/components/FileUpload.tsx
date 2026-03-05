"use client";

import { useState } from "react";
import { UploadCloud, FileText, Loader2, CheckCircle2, AlertCircle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function FileUpload() {
    const [file, setFile] = useState<File | null>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState(false);
    const [dragging, setDragging] = useState(false);

    const handleFileChange = (selectedFile: File) => {
        if (!selectedFile.name.match(/\.(csv|txt)$/)) {
            setError("Only CSV or TXT files are allowed.");
            return;
        }

        setError(null);
        setFile(selectedFile);
    };

    const handleUpload = async () => {
        if (!file) {
            setError("Please select a file first.");
            return;
        }

        setLoading(true);
        setError(null);
        setSuccess(false);

        try {
            const formData = new FormData();
            formData.append("file", file);

            const response = await fetch("http://localhost:4000/api/files/upload", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.error || "Upload failed");
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);

            const a = document.createElement("a");
            a.href = url;
            a.download = "sorted_users.csv";
            document.body.appendChild(a);
            a.click();
            a.remove();

            window.URL.revokeObjectURL(url);

            setSuccess(true);
            setFile(null);

        } catch (err: any) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="space-y-6">

            {/* Drag & Drop Area */}
            <motion.div
                onDragOver={(e) => {
                    e.preventDefault();
                    setDragging(true);
                }}
                onDragLeave={() => setDragging(false)}
                onDrop={(e) => {
                    e.preventDefault();
                    setDragging(false);
                    if (e.dataTransfer.files.length) {
                        handleFileChange(e.dataTransfer.files[0]);
                    }
                }}
                animate={{
                    borderColor: dragging
                        ? "#22d3ee"
                        : file
                            ? "#4ade80"
                            : "#374151"
                }}
                className="relative flex flex-col items-center justify-center border-2 border-dashed rounded-2xl p-10 transition-all duration-300 bg-white/5 backdrop-blur-md"
            >
                <input
                    type="file"
                    accept=".csv,.txt"
                    onChange={(e) => e.target.files && handleFileChange(e.target.files[0])}
                    className="absolute inset-0 opacity-0 cursor-pointer"
                />

                <AnimatePresence mode="wait">
                    {file ? (
                        <motion.div
                            key="file"
                            initial={{ opacity: 0, scale: 0.9 }}
                            animate={{ opacity: 1, scale: 1 }}
                            exit={{ opacity: 0 }}
                            className="flex flex-col items-center"
                        >
                            <FileText className="w-12 h-12 text-green-400 mb-3" />
                            <p className="text-sm font-semibold text-green-300">
                                {file.name}
                            </p>
                            <p className="text-xs text-gray-400">
                                {(file.size / 1024).toFixed(2)} KB
                            </p>
                        </motion.div>
                    ) : (
                        <motion.div
                            key="empty"
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="flex flex-col items-center"
                        >
                            <UploadCloud className="w-12 h-12 text-cyan-400 mb-3" />
                            <p className="text-sm font-medium text-gray-200">
                                Drag & drop your file here
                            </p>
                            <p className="text-xs text-gray-400">
                                or click to browse (CSV or TXT)
                            </p>
                        </motion.div>
                    )}
                </AnimatePresence>
            </motion.div>

            {/* Upload Button */}
            <motion.button
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
                onClick={handleUpload}
                disabled={!file || loading}
                className="w-full flex items-center justify-center gap-2 py-3 rounded-xl font-semibold
                bg-gradient-to-r from-purple-600 via-cyan-500 to-blue-600
                hover:shadow-lg hover:shadow-cyan-500/30
                transition-all duration-300
                disabled:opacity-40 disabled:cursor-not-allowed"
            >
                {loading ? (
                    <>
                        <Loader2 className="animate-spin w-4 h-4" />
                        Processing...
                    </>
                ) : (
                    "Upload & Sort"
                )}
            </motion.button>

            {/* Success Message */}
            <AnimatePresence>
                {success && (
                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0 }}
                        className="flex items-center gap-2 text-green-400 text-sm"
                    >
                        <CheckCircle2 className="w-4 h-4" />
                        File processed successfully!
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Error Message */}
            <AnimatePresence>
                {error && (
                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0 }}
                        className="flex items-center gap-2 text-red-400 text-sm"
                    >
                        <AlertCircle className="w-4 h-4" />
                        {error}
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
}