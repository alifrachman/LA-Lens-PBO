-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Jun 2021 pada 17.14
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `la_lens`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `katalog_barang`
--

CREATE TABLE `katalog_barang` (
  `id_barang` int(5) NOT NULL,
  `nama_barang` varchar(100) NOT NULL,
  `harga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `katalog_barang`
--

INSERT INTO `katalog_barang` (`id_barang`, `nama_barang`, `harga`) VALUES
(2001, 'Tripod', '30000'),
(2002, 'Stabilizer', '200000'),
(2003, 'Filter Camera', '20000'),
(2004, 'Lensa Fix', '30000'),
(2005, 'Clip On', '12000'),
(2006, 'Mic Boom', '350000'),
(2007, 'Flash Head', '35000'),
(1001, 'Cannon DSLR', '80000'),
(1002, 'Fujifilm Mirrorless', '90000'),
(1003, 'Sonny DSLR', '70000'),
(1004, 'Olympus DSLR', '85000'),
(1005, 'Sonny 4K HandyCam', '100000');

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` bigint(20) NOT NULL,
  `id_barang` varchar(4) NOT NULL,
  `tanggal_sewa` varchar(100) NOT NULL,
  `tanggal_kembali` varchar(100) DEFAULT NULL,
  `nama_pelanggan` varchar(100) CHARACTER SET utf8 NOT NULL,
  `jaminan` varchar(50) NOT NULL,
  `alamat` varchar(200) NOT NULL,
  `no_telp` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `username` varchar(30) NOT NULL,
  `nama_user` varchar(100) NOT NULL,
  `no_telp_user` varchar(14) NOT NULL,
  `alamat_user` varchar(200) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`username`, `nama_user`, `no_telp_user`, `alamat_user`, `password`) VALUES
('admin', 'Admin', '0888888888888', 'Jember', 'admin1234');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` bigint(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
