import argparse
import ZTFSchedule
import ScheduleAnimation
import FullLoc

parser = argparse.ArgumentParser()

FUNC = {'ZTF_Schedule': ZTFSchedule.ZTF_Schedule, 'full_sch_ani': ScheduleAnimation.full_sch_ani, 'schedule_event' : FullLoc.schedule_event}
parser.add_argument('--command', choices = FUNC.keys())

parser.add_argument('--prob', help = 'Enter prob')
parser.add_argument('--start_time', help = 'Enter Start Time')
parser.add_argument('--end_time', help = 'Enter End Time')
parser.add_argument('--result_path', help = 'Enter result path')
parser.add_argument('--skymap_path', help = 'Enter skymap_path')
parser.add_argument('--ns_total', help = 'Enter ns_total')
parser.add_argument('--ew_total', help = 'Enter ew_total')
parser.add_argument('--exptime', help = 'Enter exptime')
parser.add_argument('--fields', help = 'Enter fields')
parser.add_argument('--footprints_healpix', help = 'Enter footprints_healpix')
parser.add_argument('--slew_speed', help = 'Enter slew_speed')
parser.add_argument('--slew_accel', help = 'Enter slew_accel')
parser.add_argument('--filttime', help = 'Enter filttime')
parser.add_argument('--site', help = 'Enter site')
parser.add_argument('--constr', help = 'Enter constr')


args = parser.parse_args()
func = FUNC[args.command]
if args.command == 'ZTF_Schedule' :
    func(args.prob, args.start_time, args.end_time)
elif args.command == 'full_sch_ani' :
    func(args.result_path, args.skymap_path, args.ns_total, args.ew_total)
elif args.command == 'schedule_event' :
    func(args.prob, args.start_time, args.end_time, args.exptime, args.fields, args.footprints_healpix, args.slew_speed, ars.slew_accel, args.filttime, args.site, args.constr)
