# 08 — Infrastructure

## Preferred Provider

Vultr.

## MVP Infrastructure

For the first version, one VPS is enough:

```text
VPS #1: App Server
- Ubuntu 24.04 LTS
- Docker
- Docker Compose
- Reverse proxy
- Frontend
- Backend
- PostgreSQL
- Node Exporter
```

## More Secure Future Infrastructure

```text
VPS #1: App Server
- Reverse proxy
- Frontend
- Backend

VPS #2: Database Server
- PostgreSQL
- no public access

VPS #3: Monitoring Server
- Prometheus
- Grafana
- Loki
```

## Region Selection

Possible Vultr regions to test from Uzbekistan:

```text
Frankfurt
Warsaw
Delhi NCR
Tel Aviv
Singapore
```

Do not choose only by geography. Test real latency from the 21 School network.

## Latency Test Commands

```bash
ping -c 20 <test-ip>
traceroute <test-ip>
curl -o /dev/null -s -w "time_total=%{time_total}\n" https://example.com/health
```

## Acceptable Latency

For this project:

```text
under 80 ms     excellent
80–150 ms       good
150–220 ms      acceptable
220+ ms         not ideal, but still usable
```

This system is not a game or video call. Button actions and dashboards can work fine with moderate latency.

## Basic Server Hardening

Recommended first setup:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y ufw fail2ban curl git
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow from <YOUR_IP>/32 to any port 22 proto tcp
sudo ufw enable
```

Replace `<YOUR_IP>` with trusted admin IP.
